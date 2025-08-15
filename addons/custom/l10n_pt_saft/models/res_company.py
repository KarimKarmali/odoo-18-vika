# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Campos específicos para SAF-T
    saft_tax_registration_number = fields.Char(
        string='Tax Registration Number',
        help='Tax registration number for SAF-T reporting',
        compute='_compute_saft_tax_registration_number',
        store=True
    )
    saft_legal_form = fields.Char(
        string='Legal Form',
        help='Legal form of the company for SAF-T'
    )
    saft_company_registration_number = fields.Char(
        string='Company Registration Number',
        help='Company registration number (Matrícula) for SAF-T'
    )

    @api.depends('vat')
    def _compute_saft_tax_registration_number(self):
        for company in self:
            company.saft_tax_registration_number = company.vat or ''
