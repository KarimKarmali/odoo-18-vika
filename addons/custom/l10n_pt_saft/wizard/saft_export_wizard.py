# -*- coding: utf-8 -*-

import base64
import datetime
import hashlib
import xml.etree.ElementTree as ET
from xml.dom import minidom

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaftExportWizard(models.TransientModel):
    _name = 'l10n.pt.saft.export.wizard'
    _description = 'SAF-T Export Wizard for Portugal'

    company_id = fields.Many2one(
        'res.company', 
        string='Company',
        required=True,
        default=lambda self: self.env.company
    )
    date_from = fields.Date(
        string='Start Date',
        required=True,
        default=lambda self: fields.Date.today().replace(day=1)
    )
    date_to = fields.Date(
        string='End Date', 
        required=True,
        default=lambda self: (fields.Date.today().replace(day=1) + datetime.timedelta(days=32)).replace(day=1) - datetime.timedelta(days=1)
    )
    export_type = fields.Selection([
        ('accounting', 'Accounting (Contabilidade)'),
        ('invoicing', 'Invoicing (Faturação)'),
        ('both', 'Both (Ambos)')
    ], string='Export Type', default='both', required=True)
    
    # Arquivo gerado
    saft_file = fields.Binary(string='SAF-T File')
    saft_filename = fields.Char(string='Filename')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('exported', 'Exported')
    ], default='draft')

    def action_generate_saft(self):
        """Gerar arquivo SAF-T"""
        self.ensure_one()
        
        # Validações
        self._validate_data()
        
        # Gerar XML
        xml_content = self._generate_saft_xml()
        
        # Criar arquivo
        filename = f"SAF-T_PT_{self.company_id.vat or 'NoVAT'}_{self.date_from.strftime('%Y%m')}.xml"
        
        self.write({
            'saft_file': base64.b64encode(xml_content.encode('utf-8')),
            'saft_filename': filename,
            'state': 'exported'
        })
        
        # Retornar ação para download
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'new',
            'context': {'download_ready': True}
        }

    def _validate_data(self):
        """Validar dados antes de gerar SAF-T"""
        errors = []
        
        # Validar empresa
        if not self.company_id.vat:
            errors.append(_("Company VAT number is required"))
        
        if not self.company_id.street:
            errors.append(_("Company address is required"))
            
        # Validar período
        if self.date_from > self.date_to:
            errors.append(_("Start date must be before end date"))
            
        # Verificar se há movimentos no período
        moves = self.env['account.move'].search([
            ('company_id', '=', self.company_id.id),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to),
            ('state', '=', 'posted')
        ])
        
        if not moves:
            errors.append(_("No accounting entries found for the selected period"))
            
        if errors:
            raise UserError('\n'.join(errors))

    def _generate_saft_xml(self):
        """Gerar conteúdo XML do SAF-T"""
        
        # Criar elemento raiz
        root = ET.Element('AuditFile', xmlns="urn:OECD:StandardAuditFile-Tax:PT_1.04_01")
        
        # Header
        header = self._create_header(root)
        
        # Master Files
        master_files = self._create_master_files(root)
        
        # General Ledger Entries (se tipo = accounting ou both)
        if self.export_type in ['accounting', 'both']:
            self._create_general_ledger_entries(root)
            
        # Source Documents (se tipo = invoicing ou both)
        if self.export_type in ['invoicing', 'both']:
            self._create_source_documents(root)
        
        # Converter para string XML formatada
        rough_string = ET.tostring(root, encoding='unicode')
        try:
            reparsed = minidom.parseString(rough_string)
            return reparsed.toprettyxml(indent="  ", encoding=None)
        except Exception:
            # Fallback se minidom falhar
            return rough_string

    def _create_header(self, root):
        """Criar secção Header do SAF-T"""
        header = ET.SubElement(root, 'Header')
        
        ET.SubElement(header, 'AuditFileVersion').text = '1.04_01'
        ET.SubElement(header, 'CompanyID').text = self.company_id.vat or ''
        ET.SubElement(header, 'TaxRegistrationNumber').text = self.company_id.vat or ''
        ET.SubElement(header, 'TaxAccountingBasis').text = 'F'  # Faturação
        ET.SubElement(header, 'CompanyName').text = self.company_id.name or ''
        
        # Endereço da empresa
        company_address = ET.SubElement(header, 'CompanyAddress')
        ET.SubElement(company_address, 'AddressDetail').text = self.company_id.street or ''
        ET.SubElement(company_address, 'City').text = self.company_id.city or ''
        ET.SubElement(company_address, 'PostalCode').text = self.company_id.zip or ''
        ET.SubElement(company_address, 'Country').text = 'PT'
        
        ET.SubElement(header, 'FiscalYear').text = str(self.date_from.year)
        ET.SubElement(header, 'StartDate').text = self.date_from.strftime('%Y-%m-%d')
        ET.SubElement(header, 'EndDate').text = self.date_to.strftime('%Y-%m-%d')
        ET.SubElement(header, 'CurrencyCode').text = 'EUR'
        ET.SubElement(header, 'DateCreated').text = fields.Datetime.now().strftime('%Y-%m-%d')
        ET.SubElement(header, 'ProductID').text = f'Odoo/VK Commodities'
        ET.SubElement(header, 'ProductVersion').text = '18.0'
        
        return header

    def _create_master_files(self, root):
        """Criar secção MasterFiles do SAF-T"""
        master_files = ET.SubElement(root, 'MasterFiles')
        
        # General Ledger Accounts
        general_ledger_accounts = ET.SubElement(master_files, 'GeneralLedgerAccounts')
        
        accounts = self.env['account.account'].search([
            ('deprecated', '=', False)
        ])
        
        for account in accounts:
            account_elem = ET.SubElement(general_ledger_accounts, 'Account')
            ET.SubElement(account_elem, 'AccountID').text = account.code
            ET.SubElement(account_elem, 'AccountDescription').text = account.name
            ET.SubElement(account_elem, 'StandardAccountID').text = account.code
            ET.SubElement(account_elem, 'GroupingCategory').text = self._get_grouping_category(account)
            ET.SubElement(account_elem, 'GroupingCode').text = account.code[:2] if len(account.code) >= 2 else account.code
            ET.SubElement(account_elem, 'TaxonomyCode').text = account.code
            
        # Customers
        customers = ET.SubElement(master_files, 'Customers')
        customer_partners = self.env['res.partner'].search([
            ('customer_rank', '>', 0)
        ])
        
        for partner in customer_partners:
            customer = ET.SubElement(customers, 'Customer')
            ET.SubElement(customer, 'CustomerID').text = str(partner.id)
            ET.SubElement(customer, 'AccountID').text = '211'  # Conta padrão clientes
            ET.SubElement(customer, 'CustomerTaxID').text = partner.vat or ''
            ET.SubElement(customer, 'CompanyName').text = partner.name or ''
            
            # Endereço do cliente
            address = ET.SubElement(customer, 'BillingAddress')
            ET.SubElement(address, 'AddressDetail').text = partner.street or ''
            ET.SubElement(address, 'City').text = partner.city or ''
            ET.SubElement(address, 'PostalCode').text = partner.zip or ''
            ET.SubElement(address, 'Country').text = partner.country_id.code if partner.country_id else 'PT'
            
        # Suppliers
        suppliers = ET.SubElement(master_files, 'Suppliers')
        supplier_partners = self.env['res.partner'].search([
            ('supplier_rank', '>', 0)
        ])
        
        for partner in supplier_partners:
            supplier = ET.SubElement(suppliers, 'Supplier')
            ET.SubElement(supplier, 'SupplierID').text = str(partner.id)
            ET.SubElement(supplier, 'AccountID').text = '221'  # Conta padrão fornecedores
            ET.SubElement(supplier, 'SupplierTaxID').text = partner.vat or ''
            ET.SubElement(supplier, 'CompanyName').text = partner.name or ''
            
            # Endereço do fornecedor
            address = ET.SubElement(supplier, 'SupplierAddress')
            ET.SubElement(address, 'AddressDetail').text = partner.street or ''
            ET.SubElement(address, 'City').text = partner.city or ''
            ET.SubElement(address, 'PostalCode').text = partner.zip or ''
            ET.SubElement(address, 'Country').text = partner.country_id.code if partner.country_id else 'PT'
            
        # Tax Table
        tax_table = ET.SubElement(master_files, 'TaxTable')
        taxes = self.env['account.tax'].search([
            '|', ('company_id', '=', self.company_id.id), ('company_id', '=', False)
        ])
        
        for tax in taxes:
            tax_elem = ET.SubElement(tax_table, 'TaxTableEntry')
            ET.SubElement(tax_elem, 'TaxType').text = 'IVA'
            ET.SubElement(tax_elem, 'TaxCountryRegion').text = 'PT'
            ET.SubElement(tax_elem, 'TaxCode').text = tax.name
            ET.SubElement(tax_elem, 'Description').text = tax.name
            ET.SubElement(tax_elem, 'TaxPercentage').text = str(tax.amount)
            
        return master_files

    def _create_general_ledger_entries(self, root):
        """Criar secção GeneralLedgerEntries do SAF-T"""
        gl_entries = ET.SubElement(root, 'GeneralLedgerEntries')
        
        # Buscar movimentos contabilísticos do período
        moves = self.env['account.move'].search([
            ('company_id', '=', self.company_id.id),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to),
            ('state', '=', 'posted')
        ], order='date, name')
        
        # Agrupar por diário
        journals = moves.mapped('journal_id')
        
        for journal in journals:
            journal_moves = moves.filtered(lambda m: m.journal_id == journal)
            
            journal_elem = ET.SubElement(gl_entries, 'Journal')
            ET.SubElement(journal_elem, 'JournalID').text = journal.code
            ET.SubElement(journal_elem, 'Description').text = journal.name
            
            # Transações do diário
            for move in journal_moves:
                transaction = ET.SubElement(journal_elem, 'Transaction')
                ET.SubElement(transaction, 'TransactionID').text = move.name
                ET.SubElement(transaction, 'Period').text = str(move.date.month)
                ET.SubElement(transaction, 'TransactionDate').text = move.date.strftime('%Y-%m-%d')
                ET.SubElement(transaction, 'SourceID').text = journal.code
                ET.SubElement(transaction, 'Description').text = move.ref or move.name
                ET.SubElement(transaction, 'DocArchivalNumber').text = move.name
                
                # Linhas da transação
                for line in move.line_ids:
                    line_elem = ET.SubElement(transaction, 'Line')
                    ET.SubElement(line_elem, 'RecordID').text = str(line.id)
                    ET.SubElement(line_elem, 'AccountID').text = line.account_id.code
                    ET.SubElement(line_elem, 'SourceDocumentID').text = move.name
                    
                    if line.partner_id:
                        if line.partner_id.customer_rank > 0:
                            ET.SubElement(line_elem, 'CustomerID').text = str(line.partner_id.id)
                        elif line.partner_id.supplier_rank > 0:
                            ET.SubElement(line_elem, 'SupplierID').text = str(line.partner_id.id)
                    
                    ET.SubElement(line_elem, 'Description').text = line.name or ''
                    
                    if line.debit > 0:
                        ET.SubElement(line_elem, 'DebitAmount').text = f"{line.debit:.2f}"
                    if line.credit > 0:
                        ET.SubElement(line_elem, 'CreditAmount').text = f"{line.credit:.2f}"
                        
        return gl_entries

    def _create_source_documents(self, root):
        """Criar secção SourceDocuments do SAF-T"""
        source_documents = ET.SubElement(root, 'SourceDocuments')
        
        # Sales Invoices
        sales_invoices = ET.SubElement(source_documents, 'SalesInvoices')
        
        invoices = self.env['account.move'].search([
            ('company_id', '=', self.company_id.id),
            ('move_type', 'in', ['out_invoice', 'out_refund']),
            ('date', '>=', self.date_from),
            ('date', '<=', self.date_to),
            ('state', '=', 'posted')
        ], order='date, name')
        
        ET.SubElement(sales_invoices, 'NumberOfEntries').text = str(len(invoices))
        ET.SubElement(sales_invoices, 'TotalDebit').text = f"{sum(invoices.mapped('amount_total')):.2f}"
        ET.SubElement(sales_invoices, 'TotalCredit').text = "0.00"
        
        for invoice in invoices:
            invoice_elem = ET.SubElement(sales_invoices, 'Invoice')
            ET.SubElement(invoice_elem, 'InvoiceNo').text = invoice.name
            ET.SubElement(invoice_elem, 'DocumentStatus').text = 'N'  # Normal
            ET.SubElement(invoice_elem, 'Hash').text = self._generate_hash(invoice)
            ET.SubElement(invoice_elem, 'InvoiceDate').text = invoice.invoice_date.strftime('%Y-%m-%d')
            ET.SubElement(invoice_elem, 'InvoiceType').text = 'FT'  # Fatura
            ET.SubElement(invoice_elem, 'SourceID').text = invoice.invoice_user_id.name if invoice.invoice_user_id else 'Odoo'
            ET.SubElement(invoice_elem, 'SystemEntryDate').text = invoice.create_date.strftime('%Y-%m-%dT%H:%M:%S')
            ET.SubElement(invoice_elem, 'CustomerID').text = str(invoice.partner_id.id)
            
            # Linhas da fatura
            for line in invoice.invoice_line_ids:
                line_elem = ET.SubElement(invoice_elem, 'Line')
                ET.SubElement(line_elem, 'LineNumber').text = str(line.sequence)
                ET.SubElement(line_elem, 'ProductCode').text = line.product_id.default_code or str(line.product_id.id) if line.product_id else ''
                ET.SubElement(line_elem, 'ProductDescription').text = line.name or ''
                ET.SubElement(line_elem, 'Quantity').text = f"{line.quantity:.2f}"
                ET.SubElement(line_elem, 'UnitOfMeasure').text = line.product_uom_id.name if line.product_uom_id else 'UN'
                ET.SubElement(line_elem, 'UnitPrice').text = f"{line.price_unit:.2f}"
                ET.SubElement(line_elem, 'TaxPointDate').text = invoice.invoice_date.strftime('%Y-%m-%d')
                ET.SubElement(line_elem, 'Description').text = line.name or ''
                ET.SubElement(line_elem, 'CreditAmount').text = f"{line.price_subtotal:.2f}"
                
                # Impostos da linha
                if line.tax_ids:
                    tax = line.tax_ids[0]  # Primeiro imposto
                    ET.SubElement(line_elem, 'Tax', {
                        'TaxType': 'IVA',
                        'TaxCountryRegion': 'PT',
                        'TaxCode': tax.name,
                        'TaxPercentage': str(tax.amount)
                    })
            
            # Totais da fatura
            doc_totals = ET.SubElement(invoice_elem, 'DocumentTotals')
            ET.SubElement(doc_totals, 'TaxPayable').text = f"{invoice.amount_tax:.2f}"
            ET.SubElement(doc_totals, 'NetTotal').text = f"{invoice.amount_untaxed:.2f}"
            ET.SubElement(doc_totals, 'GrossTotal').text = f"{invoice.amount_total:.2f}"
            
        return source_documents

    def _get_grouping_category(self, account):
        """Determinar categoria de agrupamento da conta"""
        code = account.code
        if code.startswith('1'):
            return 'GA'  # Activo
        elif code.startswith('2'):
            return 'GP'  # Passivo
        elif code.startswith('3'):
            return 'GI'  # Inventários  
        elif code.startswith('4'):
            return 'GC'  # Capital
        elif code.startswith('5'):
            return 'GA'  # Activo fixo
        elif code.startswith('6'):
            return 'GG'  # Gastos
        elif code.startswith('7'):
            return 'GR'  # Rendimentos
        elif code.startswith('8'):
            return 'GR'  # Resultados
        else:
            return 'GO'  # Outros

    def _generate_hash(self, invoice):
        """Gerar hash da fatura (simplificado)"""
        data = f"{invoice.name}{invoice.invoice_date}{invoice.amount_total}"
        return hashlib.md5(data.encode()).hexdigest()[:32]
