# -*- coding: utf-8 -*-
{
    'name': 'Account Usability Enhancement',
    'summary': 'Enhancements for Odoo Community accounting menus and manual access',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Accounting',
    'license': 'AGPL-3',
    'description': '''
    This module provides:
    - Missing accounting menus for Odoo Community Edition
    - Access to comprehensive accounting manual
    - Enhanced usability for accounting features
    ''',
    'author': 'VIKA Team',
    'website': 'https://vika.pt',
    'depends': ['account', 'base', 'web'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'account_usability/static/src/js/manual_modal.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
