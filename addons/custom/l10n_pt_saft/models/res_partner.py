# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Campos específicos para SAF-T
    saft_customer_id = fields.Char(
        string='SAF-T Customer ID',
        help='Customer ID for SAF-T reporting',
        compute='_compute_saft_customer_id',
        store=True
    )
    saft_supplier_id = fields.Char(
        string='SAF-T Supplier ID',
        help='Supplier ID for SAF-T reporting',
        compute='_compute_saft_supplier_id',
        store=True
    )

    @api.depends('customer_rank')
    def _compute_saft_customer_id(self):
        for partner in self:
            if partner.customer_rank > 0:
                partner.saft_customer_id = str(partner.id)
            else:
                partner.saft_customer_id = ''

    @api.depends('supplier_rank')
    def _compute_saft_supplier_id(self):
        for partner in self:
            if partner.supplier_rank > 0:
                partner.saft_supplier_id = str(partner.id)
            else:
                partner.saft_supplier_id = ''
