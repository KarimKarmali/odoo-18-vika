# -*- coding: utf-8 -*-

from odoo import models, fields, tools


class TransitReport(models.Model):
    _name = 'account.transit.report'
    _description = 'Relatório de Mercadoria em Trânsito'
    _auto = False
    _rec_name = 'account_name'

    # Campos do relatório
    account_id = fields.Many2one('account.account', string='Conta')
    account_name = fields.Char('Nome da Conta')
    account_code = fields.Char('Código da Conta')
    
    partner_id = fields.Many2one('res.partner', string='Parceiro')
    partner_name = fields.Char('Nome do Parceiro')
    
    product_id = fields.Many2one('product.product', string='Produto')
    product_name = fields.Char('Nome do Produto')
    
    # Movimentos
    move_date = fields.Date('Data do Movimento')
    move_ref = fields.Char('Referência')
    move_name = fields.Char('Descrição')
    
    # Valores
    debit = fields.Monetary('Débito', currency_field='currency_id')
    credit = fields.Monetary('Crédito', currency_field='currency_id')
    balance = fields.Monetary('Saldo', currency_field='currency_id')
    
    currency_id = fields.Many2one('res.currency', string='Moeda')
    company_id = fields.Many2one('res.company', string='Empresa')

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        query = """
            CREATE OR REPLACE VIEW %s AS (
                SELECT 
                    aml.id,
                    
                    -- Conta
                    aa.id as account_id,
                    aa.name::text as account_name,
                    aa.name::text as account_code,
                    
                    -- Parceiro
                    rp.id as partner_id,
                    rp.name as partner_name,
                    
                    -- Produto
                    pp.id as product_id,
                    pt.name as product_name,
                    
                    -- Movimento
                    am.date as move_date,
                    am.ref as move_ref,
                    aml.name as move_name,
                    
                    -- Valores
                    aml.debit,
                    aml.credit,
                    aml.balance,
                    
                    -- Outros
                    am.currency_id,
                    am.company_id
                    
                FROM account_move_line aml
                JOIN account_account aa ON aml.account_id = aa.id
                JOIN account_move am ON aml.move_id = am.id
                LEFT JOIN res_partner rp ON aml.partner_id = rp.id
                LEFT JOIN product_product pp ON aml.product_id = pp.id
                LEFT JOIN product_template pt ON pp.product_tmpl_id = pt.id
                
                WHERE (aa.name::text LIKE '%%36%%' OR aa.name::text ILIKE '%%trânsito%%' OR aa.name::text ILIKE '%%transito%%')
                AND am.state = 'posted'
                AND aml.balance != 0
                
                ORDER BY am.date DESC, aa.name::text, rp.name
            )
        """ % self._table
        self.env.cr.execute(query)
