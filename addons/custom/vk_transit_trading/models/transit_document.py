# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import datetime


class TransitDocument(models.Model):
    _name = 'vk.transit.document'
    _description = 'Documento de Mercadoria em Trânsito'
    _order = 'create_date desc'
    _rec_name = 'display_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Campos principais
    name = fields.Char(
        string='Documento',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New')
    )
    
    display_name = fields.Char(
        string='Nome',
        compute='_compute_display_name',
        store=True
    )
    
    document_type = fields.Selection([
        ('purchase_transit', 'Documento Compra Trânsito (DCT)'),
        ('reception', 'Documento Receção (DR)')
    ], string='Tipo Documento', required=True)
    
    state = fields.Selection([
        ('draft', 'Rascunho'),
        ('confirmed', 'Confirmado'),
        ('in_transit', 'Em Trânsito'),
        ('received', 'Recebido'),
        ('reconciled', 'Reconciliado'),
        ('cancelled', 'Cancelado')
    ], string='Estado', default='draft', tracking=True)
    
    # Datas
    document_date = fields.Date(
        string='Data Documento',
        required=True,
        default=fields.Date.context_today
    )
    expected_arrival_date = fields.Date(
        string='Data Chegada Esperada',
        help='Data prevista de chegada da mercadoria'
    )
    actual_arrival_date = fields.Date(
        string='Data Chegada Real',
        help='Data real de chegada da mercadoria'
    )
    
    # Parceiro
    partner_id = fields.Many2one(
        'res.partner',
        string='Fornecedor/Cliente',
        required=True,
        domain="['|', ('supplier_rank', '>', 0), ('customer_rank', '>', 0)]"
    )
    
    # Referências
    purchase_order_id = fields.Many2one(
        'purchase.order',
        string='Ordem de Compra',
        help='Ordem de compra associada'
    )
    stock_picking_id = fields.Many2one(
        'stock.picking',
        string='Receção Stock',
        help='Documento de receção associado'
    )
    invoice_id = fields.Many2one(
        'account.move',
        string='Fatura',
        help='Fatura associada'
    )
    
    # Linhas do documento
    line_ids = fields.One2many(
        'vk.transit.document.line',
        'document_id',
        string='Linhas do Documento'
    )
    
    # Totais
    total_quantity = fields.Float(
        string='Quantidade Total',
        compute='_compute_totals',
        store=True
    )
    total_weight = fields.Float(
        string='Peso Total (Kg)',
        compute='_compute_totals',
        store=True
    )
    total_value = fields.Monetary(
        string='Valor Total',
        compute='_compute_totals',
        store=True,
        currency_field='currency_id'
    )
    
    # Campos de controlo
    currency_id = fields.Many2one(
        'res.currency',
        string='Moeda',
        default=lambda self: self.env.company.currency_id
    )
    company_id = fields.Many2one(
        'res.company',
        string='Empresa',
        default=lambda self: self.env.company
    )
    
    # Tracking e aging
    days_in_transit = fields.Integer(
        string='Dias em Trânsito',
        compute='_compute_days_in_transit',
        store=True
    )
    is_overdue = fields.Boolean(
        string='Em Atraso',
        compute='_compute_is_overdue',
        store=True
    )
    
    # Documento relacionado (matching)
    related_document_id = fields.Many2one(
        'vk.transit.document',
        string='Documento Relacionado',
        help='DCT relacionado com DR ou vice-versa'
    )
    
    # Observações
    notes = fields.Text(string='Observações')
    
    @api.depends('name', 'document_type', 'partner_id')
    def _compute_display_name(self):
        for record in self:
            if record.name and record.name != 'New':
                type_name = dict(record._fields['document_type'].selection).get(record.document_type, '')
                partner_name = record.partner_id.name if record.partner_id else ''
                record.display_name = f"{record.name} - {type_name} - {partner_name}"
            else:
                record.display_name = 'New Transit Document'
    
    @api.depends('line_ids.quantity', 'line_ids.weight', 'line_ids.subtotal')
    def _compute_totals(self):
        for record in self:
            record.total_quantity = sum(record.line_ids.mapped('quantity'))
            record.total_weight = sum(record.line_ids.mapped('weight'))
            record.total_value = sum(record.line_ids.mapped('subtotal'))
    
    @api.depends('document_date', 'actual_arrival_date', 'state')
    def _compute_days_in_transit(self):
        for record in self:
            if record.state in ['in_transit', 'received'] and record.document_date:
                end_date = record.actual_arrival_date or fields.Date.today()
                delta = end_date - record.document_date
                record.days_in_transit = delta.days
            else:
                record.days_in_transit = 0
    
    @api.depends('expected_arrival_date', 'actual_arrival_date', 'state')
    def _compute_is_overdue(self):
        for record in self:
            if (record.state == 'in_transit' and 
                record.expected_arrival_date and 
                not record.actual_arrival_date):
                record.is_overdue = fields.Date.today() > record.expected_arrival_date
            else:
                record.is_overdue = False
    
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if vals.get('document_type') == 'purchase_transit':
                vals['name'] = f"DCT{str(len(self.search([])) + 1).zfill(4)}"
            else:
                vals['name'] = f"DR{str(len(self.search([])) + 1).zfill(4)}"
        return super().create(vals)
    
    def action_confirm(self):
        """Confirmar documento"""
        self.ensure_one()
        if not self.line_ids:
            raise UserError(_("Não é possível confirmar documento sem linhas."))
        
        if self.document_type == 'purchase_transit':
            self.state = 'in_transit'
            # TODO: Criar movimentos contabilísticos
        else:
            self.state = 'confirmed'
        
        return True
    
    def action_receive(self):
        """Marcar como recebido"""
        self.ensure_one()
        if self.document_type != 'purchase_transit':
            raise UserError(_("Apenas DCT podem ser marcados como recebidos."))
        
        self.write({
            'state': 'received',
            'actual_arrival_date': fields.Date.today()
        })
        
        return True
    
    def action_reconcile_with_reception(self):
        """Abrir wizard para reconciliar DCT com DR"""
        self.ensure_one()
        if self.document_type != 'purchase_transit':
            raise UserError(_("Apenas DCT podem ser reconciliados."))
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reconciliar com Receção',
            'res_model': 'vk.transit.reconciliation.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_dct_id': self.id}
        }
    
    # TODO: Implementar movimentos contabilísticos numa versão futura


class TransitDocumentLine(models.Model):
    _name = 'vk.transit.document.line'
    _description = 'Linha do Documento de Trânsito'
    
    document_id = fields.Many2one(
        'vk.transit.document',
        string='Documento',
        required=True,
        ondelete='cascade'
    )
    
    product_id = fields.Many2one(
        'product.product',
        string='Produto',
        required=True
    )
    
    description = fields.Text(
        string='Descrição',
        required=True
    )
    
    quantity = fields.Float(
        string='Quantidade',
        required=True,
        default=1.0
    )
    
    uom_id = fields.Many2one(
        'uom.uom',
        string='Unidade Medida',
        required=True
    )
    
    weight = fields.Float(
        string='Peso (Kg)',
        help='Peso da linha em Kg'
    )
    
    price_unit = fields.Monetary(
        string='Preço Unitário',
        required=True,
        currency_field='currency_id'
    )
    
    subtotal = fields.Monetary(
        string='Subtotal',
        compute='_compute_subtotal',
        store=True,
        currency_field='currency_id'
    )
    
    currency_id = fields.Many2one(
        related='document_id.currency_id',
        store=True
    )
    
    # Campos para matching
    received_quantity = fields.Float(
        string='Quantidade Recebida',
        default=0.0
    )
    
    pending_quantity = fields.Float(
        string='Quantidade Pendente',
        compute='_compute_pending_quantity',
        store=True
    )
    
    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
    
    @api.depends('quantity', 'received_quantity')
    def _compute_pending_quantity(self):
        for line in self:
            line.pending_quantity = line.quantity - line.received_quantity
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.description = self.product_id.display_name
            self.uom_id = self.product_id.uom_id
            self.price_unit = self.product_id.standard_price
