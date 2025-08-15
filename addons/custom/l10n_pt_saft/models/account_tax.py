# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    # Campos específicos para SAF-T
    saft_tax_type = fields.Selection([
        ('IVA', 'IVA'),
        ('IS', 'Imposto de Selo'),
        ('IEC', 'Imposto Especial de Consumo'),
        ('OUT', 'Outros')
    ], string='SAF-T Tax Type', default='IVA')
    
    saft_tax_code = fields.Char(
        string='SAF-T Tax Code',
        help='Tax code for SAF-T reporting'
    )
    
    saft_country_region = fields.Char(
        string='SAF-T Country/Region',
        default='PT',
        help='Country or region code for SAF-T'
    )
