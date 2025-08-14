# -*- coding: utf-8 -*-
{
    'name': 'Manual VIKA - Menu Fixo',
    'summary': 'Menu permanente para o Manual de Contabilidade VIKA',
    'version': '18.0.1.0.0',
    'category': 'Documentation',
    'license': 'AGPL-3',
    'description': '''
    Este módulo garante que o menu do Manual de Contabilidade VIKA 
    aparece sempre em Accounting > Reporting, sem depender de comandos Python.
    ''',
    'author': 'VIKA Team',
    'website': 'https://vika.pt',
    'depends': ['account'],
    'data': [
        'views/manual_menu.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
