#!/usr/bin/env python3
"""
Criar Dashboard Principal com Ícones das Apps
VK Commodities - Dashboard de Navegação Principal
"""

import os
import sys
import json
from datetime import datetime

# Configuração das aplicações principais com ícones e cores
MAIN_APPS = {
    'account': {
        'name': 'Contabilidade',
        'icon': 'fa-calculator',
        'color': '#875A7B',
        'description': 'Gestão financeira e contabilística',
        'menu_id': 'account.menu_finance',
        'action': 'account.action_move_journal_line'
    },
    'sale_management': {
        'name': 'Vendas',
        'icon': 'fa-shopping-cart',
        'color': '#1f77b4',
        'description': 'Gestão de vendas e orçamentos',
        'menu_id': 'sale.sale_menu_root',
        'action': 'sale.action_orders'
    },
    'purchase': {
        'name': 'Compras',
        'icon': 'fa-shopping-bag',
        'color': '#ff7f0e',
        'description': 'Gestão de compras e fornecedores',
        'menu_id': 'purchase.menu_purchase_root',
        'action': 'purchase.purchase_rfq'
    },
    'stock': {
        'name': 'Inventário',
        'icon': 'fa-cubes',
        'color': '#2ca02c',
        'description': 'Gestão de stock e armazém',
        'menu_id': 'stock.menu_stock_root',
        'action': 'stock.action_picking_tree_all'
    },
    'mail': {
        'name': 'Discussões',
        'icon': 'fa-comments',
        'color': '#d62728',
        'description': 'Mensagens e comunicação',
        'menu_id': 'mail.menu_root_discuss',
        'action': 'mail.action_discuss'
    },
    'base_accounting_kit': {
        'name': 'Relatórios Financeiros',
        'icon': 'fa-line-chart',
        'color': '#9467bd',
        'description': 'Relatórios e análises financeiras',
        'menu_id': 'base_accounting_kit.menu_accounting_reports',
        'action': 'base_accounting_kit.action_account_report_bs'
    },
    'mis_builder': {
        'name': 'MIS Builder',
        'icon': 'fa-bar-chart',
        'color': '#8c564b',
        'description': 'Relatórios de gestão',
        'menu_id': 'mis_builder.menu_mis_report_instance',
        'action': 'mis_builder.mis_report_instance_action'
    },
    'l10n_pt_saft': {
        'name': 'SAF-T Portugal',
        'icon': 'fa-file-text-o',
        'color': '#e377c2',
        'description': 'Ficheiro SAF-T para Portugal',
        'menu_id': 'l10n_pt_saft.menu_saft_export',
        'action': 'l10n_pt_saft.action_saft_export'
    }
}

# Widgets de KPI para o dashboard
DASHBOARD_KPIS = [
    {
        'name': 'Vendas do Mês',
        'model': 'sale.order',
        'measure_field': 'amount_total',
        'domain': "[('state','in',['sale','done']),('date_order','>=',datetime.now().replace(day=1))]",
        'icon': 'fa-euro',
        'color': '#1f77b4'
    },
    {
        'name': 'Compras do Mês',
        'model': 'purchase.order',
        'measure_field': 'amount_total',
        'domain': "[('state','in',['purchase','done']),('date_order','>=',datetime.now().replace(day=1))]",
        'icon': 'fa-shopping-bag',
        'color': '#ff7f0e'
    },
    {
        'name': 'Faturas em Aberto',
        'model': 'account.move',
        'measure_field': 'amount_residual',
        'domain': "[('move_type','=','out_invoice'),('payment_state','!=','paid')]",
        'icon': 'fa-file-text',
        'color': '#d62728'
    },
    {
        'name': 'Produtos em Stock',
        'model': 'product.product',
        'measure_field': 'qty_available',
        'domain': "[('type','=','product')]",
        'icon': 'fa-cubes',
        'color': '#2ca02c'
    }
]

def create_dashboard_xml():
    """Criar XML para o dashboard principal"""
    
    xml_content = '''<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <data>
        <!-- Dashboard Principal VK Commodities -->
        <record id="vk_main_dashboard" model="ks_dashboard_ninja_board">
            <field name="name">VK Commodities - Dashboard Principal</field>
            <field name="ks_dashboard_menu_name">Dashboard Principal</field>
            <field name="ks_dashboard_top_menu_id" ref="base.menu_administration"/>
            <field name="ks_dashboard_active">True</field>
            <field name="ks_dashboard_default_template" ref="ks_dashboard_ninja.ks_blank"/>
            <field name="ks_set_interval">15</field>
            <field name="ks_dashboard_ninja_board_template">
                {
                    "ks_dashboard_manager": false,
                    "ks_dashboard_list": [],
                    "ks_dashboard_items_ids": [],
                    "ks_child_boards": [],
                    "ks_dashboard_name": "VK Commodities - Dashboard Principal",
                    "ks_dashboard_menu_name": "Dashboard Principal"
                }
            </field>
        </record>

'''

    # Adicionar widgets de aplicações
    item_id = 1
    for app_key, app_info in MAIN_APPS.items():
        xml_content += f'''
        <!-- Widget {app_info['name']} -->
        <record id="vk_dashboard_item_{app_key}" model="ks_dashboard_ninja_item">
            <field name="ks_dashboard_ninja_board_id" ref="vk_main_dashboard"/>
            <field name="name">{app_info['name']}</field>
            <field name="ks_dashboard_item_type">ks_tile</field>
            <field name="ks_icon_select">{app_info['icon']}</field>
            <field name="ks_background_color">{app_info['color']}</field>
            <field name="ks_font_color">#FFFFFF</field>
            <field name="ks_tile_info">{app_info['description']}</field>
            <field name="sequence">{item_id}</field>
            <field name="ks_actions" eval="False"/>
        </record>
'''
        item_id += 1

    # Adicionar widgets de KPI
    for kpi in DASHBOARD_KPIS:
        xml_content += f'''
        <!-- KPI {kpi['name']} -->
        <record id="vk_dashboard_kpi_{kpi['name'].lower().replace(' ', '_')}" model="ks_dashboard_ninja_item">
            <field name="ks_dashboard_ninja_board_id" ref="vk_main_dashboard"/>
            <field name="name">{kpi['name']}</field>
            <field name="ks_dashboard_item_type">ks_kpi</field>
            <field name="ks_model_id" ref="base.model_{kpi['model'].replace('.', '_')}"/>
            <field name="ks_record_count_type">count</field>
            <field name="ks_icon_select">{kpi['icon']}</field>
            <field name="ks_background_color">{kpi['color']}</field>
            <field name="ks_font_color">#FFFFFF</field>
            <field name="sequence">{item_id}</field>
        </record>
'''
        item_id += 1

    xml_content += '''
        <!-- Menu para o Dashboard Principal -->
        <menuitem id="vk_main_dashboard_menu"
                  name="Dashboard Principal"
                  parent="base.menu_administration"
                  action="ks_dashboard_ninja.ks_dashboard_ninja_action"
                  sequence="1"/>

    </data>
</odoo>
'''
    
    return xml_content

def create_dashboard_data():
    """Criar dados do dashboard"""
    
    # Criar diretório se não existir
    os.makedirs('addons/custom/vk_main_dashboard', exist_ok=True)
    os.makedirs('addons/custom/vk_main_dashboard/data', exist_ok=True)
    
    # Criar manifest
    manifest_content = '''{
    'name': 'VK Main Dashboard',
    'version': '18.0.1.0.0',
    'category': 'Dashboard',
    'summary': 'Dashboard principal com navegação por ícones',
    'description': """
        Dashboard principal da VK Commodities com ícones das aplicações
        para facilitar a navegação no sistema.
    """,
    'author': 'VK Commodities',
    'depends': ['base', 'ks_dashboard_ninja', 'account', 'sale_management', 'purchase', 'stock'],
    'data': [
        'data/dashboard_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}'''
    
    with open('addons/custom/vk_main_dashboard/__manifest__.py', 'w', encoding='utf-8') as f:
        f.write(manifest_content)
    
    # Criar __init__.py vazio
    with open('addons/custom/vk_main_dashboard/__init__.py', 'w') as f:
        f.write('# VK Main Dashboard\n')
    
    # Criar XML do dashboard
    xml_content = create_dashboard_xml()
    with open('addons/custom/vk_main_dashboard/data/dashboard_data.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print("✅ Dashboard principal criado!")
    print("📁 Localização: addons/custom/vk_main_dashboard/")
    print("\n📋 Aplicações incluídas:")
    for app_key, app_info in MAIN_APPS.items():
        print(f"  • {app_info['name']} - {app_info['description']}")
    
    print(f"\n📊 KPIs incluídos:")
    for kpi in DASHBOARD_KPIS:
        print(f"  • {kpi['name']}")
    
    return True

def create_installation_script():
    """Criar script para instalar o dashboard"""
    
    script_content = '''#!/usr/bin/env python3
"""
Instalar Dashboard Principal VK Commodities
"""

import subprocess
import sys
import os

def install_dashboard():
    """Instalar o módulo do dashboard principal"""
    
    print("🚀 Instalando Dashboard Principal VK Commodities...")
    
    try:
        # Comando para instalar o módulo
        cmd = [
            sys.executable, 
            'odoo-source/odoo-bin',
            '-c', 'config/odoo-python.conf',
            '-d', 'vk_dev',
            '-i', 'vk_main_dashboard',
            '--stop-after-init'
        ]
        
        print(f"🔧 Executando: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dashboard instalado com sucesso!")
            print("\\n📋 Próximos passos:")
            print("1. Reinicie o Odoo")
            print("2. Aceda a 'Configurações > Dashboard Principal'")
            print("3. Configure os widgets conforme necessário")
            return True
        else:
            print("❌ Erro na instalação:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    install_dashboard()
'''
    
    with open('scripts/install-main-dashboard.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("✅ Script de instalação criado: scripts/install-main-dashboard.py")

if __name__ == "__main__":
    print("🎨 Criando Dashboard Principal VK Commodities...")
    print("=" * 50)
    
    # Criar estrutura do dashboard
    if create_dashboard_data():
        create_installation_script()
        
        print("\n" + "=" * 50)
        print("✅ DASHBOARD PRINCIPAL CRIADO COM SUCESSO!")
        print("=" * 50)
        print("\n📋 Para instalar:")
        print("1. python scripts/install-main-dashboard.py")
        print("2. Reiniciar o Odoo")
        print("3. Aceder ao menu 'Dashboard Principal'")
        print("\n🎯 O dashboard incluirá:")
        print("• Ícones das aplicações principais")
        print("• KPIs de vendas, compras e stock")
        print("• Navegação visual intuitiva")
        print("• Cores personalizadas VK Commodities")
