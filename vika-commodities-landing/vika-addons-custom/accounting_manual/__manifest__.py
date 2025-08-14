# -*- coding: utf-8 -*-
{
    'name': 'VIKA Accounting Manual',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'summary': 'Manual de Contabilidade VIKA - Documentação completa dos módulos OCA',
    'description': '''
    Manual completo de contabilidade VIKA com documentação de todos os módulos instalados:
    
    • Account Usability - Missing Menus
    • MIS Builder & Budget
    • Account Financial Report  
    • InvoiceXpress Integration
    • Asset Management
    • Tax Balance
    • Partner Statement
    • E muito mais...
    
    Inclui guias de configuração, exemplos práticos e melhores práticas.
    ''',
    'author': 'VIKA Team',
    'website': 'https://vika.pt',
    'depends': ['account', 'web'],
    'data': [
        'views/manual_menu.xml',
        'views/manual_template.xml',
        'views/manual_page.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'accounting_manual/static/src/css/manual.css',
            'accounting_manual/static/src/js/manual.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
