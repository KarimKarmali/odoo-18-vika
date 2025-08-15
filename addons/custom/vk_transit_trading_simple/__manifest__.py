{
    'name': 'Mapa Mercadoria em Trânsito',
    'version': '18.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Relatório simples para consultar mercadoria em trânsito (conta 36)',
    'description': """
Mapa de Mercadoria em Trânsito
==============================

Relatório simples que mostra os saldos das contas 36x (mercadoria em trânsito).

Funcionalidades:
- Consulta movimentos da conta 36
- Agrupa por produto/fornecedor
- Mostra saldos pendentes
- Export para Excel

Desenvolvido para VK Commodities.
    """,
    'author': 'VK Commodities',
    'website': 'https://vkcommodities.pt',
    'depends': [
        'account',
        'purchase',
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/transit_report_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
