# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools


class TransitReport(models.Model):
    _name = 'vk.transit.report'
    _description = 'Relatório de Mercadoria em Trânsito'
    _auto = False
    _rec_name = 'product_name'

    # Campos principais
    id = fields.Integer('ID')
    document_id = fields.Many2one('vk.transit.document', string='Documento')
    document_name = fields.Char('Nº Documento')
    document_date = fields.Date('Data Documento')
    document_type = fields.Selection([
        ('purchase_transit', 'DCT'),
        ('reception', 'DR')
    ], string='Tipo')
    
    # Parceiro
    partner_id = fields.Many2one('res.partner', string='Fornecedor')
    partner_name = fields.Char('Nome Fornecedor')
    
    # Produto
    product_id = fields.Many2one('product.product', string='Produto')
    product_name = fields.Char('Nome Produto')
    product_category = fields.Char('Categoria')
    
    # Quantidades
    quantity_ordered = fields.Float('Qtd Encomendada')
    quantity_received = fields.Float('Qtd Recebida')
    quantity_pending = fields.Float('Qtd Pendente')
    
    # Valores
    unit_price = fields.Monetary('Preço Unit.', currency_field='currency_id')
    total_value = fields.Monetary('Valor Total', currency_field='currency_id')
    pending_value = fields.Monetary('Valor Pendente', currency_field='currency_id')
    
    # Datas e controlo
    expected_date = fields.Date('Data Esperada')
    actual_date = fields.Date('Data Real')
    days_transit = fields.Integer('Dias Trânsito')
    is_overdue = fields.Boolean('Em Atraso')
    
    # Estado
    state = fields.Selection([
        ('draft', 'Rascunho'),
        ('in_transit', 'Em Trânsito'),
        ('received', 'Recebido'),
        ('reconciled', 'Reconciliado')
    ], string='Estado')
    
    # Outros
    currency_id = fields.Many2one('res.currency', string='Moeda')
    company_id = fields.Many2one('res.company', string='Empresa')
    
    # TODO: Implementar view SQL numa versão futura
    # Comentado para evitar erros durante instalação inicial
    # def init(self):
    #     tools.drop_view_if_exists(self.env.cr, self._table)
    #     pass


# TODO: Implementar relatório summary numa versão futura
# class TransitSummaryReport(models.Model):
#     _name = 'vk.transit.summary'
