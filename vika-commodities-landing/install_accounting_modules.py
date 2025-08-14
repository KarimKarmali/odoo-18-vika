#!/usr/bin/env python3
import sys
import os

# Adicionar o diretório do Odoo ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'odoo'))

import odoo
from odoo import api, SUPERUSER_ID
from odoo.tools import config

# Configurar o Odoo
config.parse_config(['-c', 'odoo_vika_18.conf', '-d', 'vika_odoo18'])

# Inicializar o registry
registry = odoo.registry('vika_odoo18')

print("=== INSTALANDO MÓDULOS DE CONTABILIDADE ===")

# Lista de módulos para instalar
modules_to_install = [
    'account_financial_report',
    'account_tax_balance', 
    'partner_statement',
    'account_asset_management',
    'account_move_template',
    'account_fiscal_year'
]

with registry.cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Atualizar lista de módulos
    print("✓ Atualizando lista de módulos...")
    env['ir.module.module'].update_list()
    
    for module_name in modules_to_install:
        print(f"\n--- Processando módulo: {module_name} ---")
        
        # Buscar o módulo
        module = env['ir.module.module'].search([('name', '=', module_name)])
        
        if not module:
            print(f"⚠ Módulo '{module_name}' não encontrado!")
            continue
            
        print(f"✓ Módulo encontrado: {module.name}")
        print(f"  Estado: {module.state}")
        
        if module.state == 'installed':
            print(f"✓ Já instalado!")
        elif module.state in ['uninstalled', 'to install']:
            try:
                print(f"🔄 Instalando...")
                module.button_immediate_install()
                print(f"✅ Instalado com sucesso!")
            except Exception as e:
                print(f"❌ Erro: {str(e)}")

print("\n=== INSTALAÇÃO CONCLUÍDA ===")
print("Reinicie o servidor e acesse Contabilidade > Relatórios")