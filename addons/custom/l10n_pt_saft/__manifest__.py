# -*- coding: utf-8 -*-
{
    'name': 'SAF-T Portugal (VK Commodities)',
    'version': '18.0.1.1.0',
    'category': 'Accounting/Localizations',
    'summary': 'SAF-T (Standard Audit File for Tax purposes) for Portugal - Monthly Compliance',
    'description': """
SAF-T Portugal for Odoo 18
===========================

Generate monthly SAF-T files for Portuguese Tax Authority (AT) compliance.

Features:
- ✅ Monthly SAF-T generation (required by AT until 5th of following month)
- ✅ XML file compatible with Portuguese Tax Authority
- ✅ Company and partner data for SAF-T
- ✅ Account and tax mapping for SAF-T
- ✅ Easy wizard interface in Accounting > Reporting
- ✅ Automatic validation before export

Legal Requirements:
- Monthly submission until 5th of following month
- XML format according to AT specifications
- All accounting and invoicing data included

Developed for VK Commodities based on Portuguese legal requirements.
    """,
    'author': 'VK Commodities',
    'website': 'https://vkcommodities.pt',
    'depends': [
        'account',
        'l10n_pt_vat',
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company_view.xml',
        'views/res_partner_view.xml', 
        'views/account_tax_view.xml',
        'views/account_journal_view.xml',
        'views/saft_export_history_view_simple.xml',
        'wizard/saft_export_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
