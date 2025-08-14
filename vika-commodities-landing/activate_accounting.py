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

print("=== ATIVANDO MÓDULO DE CONTABILIDADE ===")

with registry.cursor() as cr:
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Verificar módulos instalados
    installed_modules = env['ir.module.module'].search([
        ('state', '=', 'installed'),
        ('name', 'in', ['account', 'account_financial_report', 'base'])
    ])
    
    print("Módulos instalados:")
    for module in installed_modules:
        print(f"  ✓ {module.name}: {module.shortdesc}")
    
    # Verificar usuário admin
    admin_user = env['res.users'].search([('login', '=', 'admin')])
    if admin_user:
        print(f"\n✓ Usuário admin encontrado: {admin_user.name}")
        
        # Verificar grupos do usuário
        groups = admin_user.groups_id
        print(f"Grupos do usuário ({len(groups)}):")
        for group in groups:
            print(f"  - {group.name} ({group.category_id.name if group.category_id else 'Sem categoria'})")
        
        # Adicionar grupo de contabilidade se não tiver
        accounting_groups = env['res.groups'].search([
            '|', ('name', 'ilike', 'billing'),
            ('name', 'ilike', 'accounting')
        ])
        
        print(f"\nGrupos de contabilidade disponíveis:")
        for group in accounting_groups:
            print(f"  - {group.name}")
            if group not in admin_user.groups_id:
                print(f"    → Adicionando ao usuário admin")
                admin_user.groups_id = [(4, group.id)]
        
        # Verificar se é superusuário
        if env.ref('base.group_system') not in admin_user.groups_id:
            print("→ Adicionando permissões de administrador")
            admin_user.groups_id = [(4, env.ref('base.group_system').id)]
    
    # Verificar menus disponíveis
    accounting_menus = env['ir.ui.menu'].search([
        ('name', 'ilike', 'accounting')
    ])
    
    print(f"\nMenus de contabilidade encontrados ({len(accounting_menus)}):")
    for menu in accounting_menus:
        print(f"  - {menu.name} (ID: {menu.id}) - Ativo: {menu.active}")
        if not menu.active:
            menu.active = True
            print(f"    → Menu ativado")

print("\n=== CONCLUÍDO ===")
print("1. Faça logout e login novamente")
print("2. Limpe o cache do navegador (Ctrl+F5)")
print("3. Verifique se o menu Contabilidade aparece")
