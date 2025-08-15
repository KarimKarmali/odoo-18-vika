# -*- coding: utf-8 -*-
{
    'name': 'VK Transit Trading - Mercadoria em Trânsito',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Trading',
    'summary': 'Sistema completo para trading without warehouse - Mercadoria em Trânsito',
    'description': """
VK Transit Trading - Commodities em Trânsito
=============================================

Sistema especializado para trading de commodities sem armazém físico.

Funcionalidades:
================

📦 **DOCUMENTOS ESPECÍFICOS:**
- Documento de Compra em Trânsito (DCT)
- Documento de Receção (DR)
- Matching automático DCT ↔ DR

📊 **RELATÓRIOS ESPECIALIZADOS:**
- Mapa de Mercadoria em Trânsito
- Aging Report de Trânsito
- Reconciliação DCT vs DR
- Dashboard de KPIs

💰 **CONTAS CONTABILÍSTICAS:**
- 36.1 - Matérias Primas em Trânsito
- 36.2 - Produtos Acabados em Trânsito
- Automação de movimentos contabilísticos

🔍 **CONTROLOS:**
- Alertas de mercadoria em atraso
- Validações de quantidades
- Auditoria completa de movimentos

Desenvolvido especialmente para VK Commodities - Trading Operations.
    """,
    'author': 'VK Commodities',
    'website': 'https://vkcommodities.pt',
    'depends': [
        'purchase',
        'stock',
        'account',
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/account_account_data.xml',
        'views/transit_document_view.xml',
        # 'reports/transit_report_view.xml', # TODO: Descomentar quando relatório estiver funcional
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
