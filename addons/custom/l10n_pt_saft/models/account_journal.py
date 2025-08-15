# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    # Campos específicos para SAF-T
    saft_journal_id = fields.Char(
        string='SAF-T Journal ID',
        help='Journal ID for SAF-T reporting',
        compute='_compute_saft_journal_id',
        store=True
    )

    @api.depends('code')
    def _compute_saft_journal_id(self):
        for journal in self:
            journal.saft_journal_id = journal.code or str(journal.id)
