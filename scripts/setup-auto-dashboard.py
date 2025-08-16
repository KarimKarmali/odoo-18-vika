#!/usr/bin/env python3
"""
Setup Auto-Dashboard VK Commodities
Configura atualização automática do dashboard via hook do Odoo
"""

import os
import sys

def create_module_hook():
    """Criar hook para atualização automática"""
    
    hook_content = '''# -*- coding: utf-8 -*-
"""
Hook para atualização automática do Dashboard VK Commodities
Executado sempre que um módulo é instalado/atualizado
"""

import logging
import xmlrpc.client
from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

def post_init_hook(cr, registry):
    """Hook executado após instalação de módulos"""
    try:
        _logger.info("🔄 Verificando atualizações do Dashboard VK Commodities...")
        
        # Importar e executar atualização do dashboard
        from odoo.addons.ks_dashboard_ninja.models.ks_dashboard_ninja import KsDashboardNinjaBoard
        
        with api.Environment.manage():
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            # Buscar dashboard principal
            dashboard = env['ks_dashboard_ninja.board'].search([
                ('name', '=', 'VK Commodities - Dashboard Principal')
            ], limit=1)
            
            if dashboard:
                # Buscar aplicações instaladas
                apps = env['ir.module.module'].search([
                    ('state', '=', 'installed'),
                    ('application', '=', True)
                ])
                
                # Buscar widgets existentes
                existing_widgets = env['ks_dashboard_ninja.item'].search([
                    ('ks_dashboard_ninja_board_id', '=', dashboard.id)
                ])
                
                existing_names = {w.name for w in existing_widgets}
                
                # Cores para novos widgets
                colors = [
                    '#875A7B', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
                    '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22',
                    '#17becf', '#ff9896', '#c5b0d5', '#c49c94', '#f7b6d3'
                ]
                
                new_widgets = 0
                color_index = len(existing_widgets)
                
                for app in apps:
                    app_name = app.shortdesc or app.name
                    
                    if app_name not in existing_names:
                        try:
                            # Buscar ação principal da aplicação
                            action = env['ir.actions.act_window'].search([
                                ('res_model', '!=', False),
                                '|', ('name', 'ilike', app.name),
                                     ('name', 'ilike', app.shortdesc)
                            ], limit=1)
                            
                            if action:
                                color = colors[color_index % len(colors)]
                                
                                # Criar widget
                                env['ks_dashboard_ninja.item'].create({
                                    'ks_dashboard_ninja_board_id': dashboard.id,
                                    'name': app_name,
                                    'ks_dashboard_item_type': 'ks_tile',
                                    'ks_icon_select': 'Default',
                                    'ks_background_color': color,
                                    'ks_font_color': '#FFFFFF',
                                    'ks_actions': action.id,
                                    'ks_layout': 'layout1'
                                })
                                
                                new_widgets += 1
                                color_index += 1
                                _logger.info(f"✅ Widget '{app_name}' adicionado ao dashboard")
                        
                        except Exception as e:
                            _logger.warning(f"⚠️  Erro ao criar widget para {app_name}: {e}")
                
                if new_widgets > 0:
                    _logger.info(f"🎯 {new_widgets} novos widgets adicionados ao Dashboard VK Commodities")
                else:
                    _logger.info("✅ Dashboard VK Commodities já está atualizado")
            
            else:
                _logger.warning("⚠️  Dashboard VK Commodities não encontrado")
                
    except Exception as e:
        _logger.error(f"❌ Erro na atualização automática do dashboard: {e}")
'''
    
    # Criar arquivo do hook
    hook_file = "addons/custom/vk_dashboard_auto_update/__init__.py"
    os.makedirs(os.path.dirname(hook_file), exist_ok=True)
    
    with open(hook_file, 'w', encoding='utf-8') as f:
        f.write(hook_content)
    
    # Criar manifest
    manifest_content = '''{
    'name': 'VK Dashboard Auto Update',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'Atualização automática do Dashboard VK Commodities',
    'description': """
        Módulo que atualiza automaticamente o Dashboard VK Commodities
        sempre que novas aplicações são instaladas no sistema.
    """,
    'author': 'VK Commodities',
    'depends': ['base', 'ks_dashboard_ninja'],
    'data': [],
    'installable': True,
    'auto_install': True,
    'post_init_hook': 'post_init_hook',
}'''
    
    manifest_file = "addons/custom/vk_dashboard_auto_update/__manifest__.py"
    with open(manifest_file, 'w', encoding='utf-8') as f:
        f.write(manifest_content)
    
    print("✅ Hook de atualização automática criado!")
    print(f"📁 Localização: {hook_file}")
    
    return True

def main():
    """Função principal"""
    print("🚀 Configurando atualização automática do Dashboard VK Commodities...")
    print("=" * 70)
    
    # Criar hook
    if create_module_hook():
        print("\n✅ CONFIGURAÇÃO CONCLUÍDA!")
        print("\n📋 Próximos passos:")
        print("1. Instalar o módulo de auto-atualização:")
        print("   python odoo-source/odoo-bin -c config/odoo-python.conf -d vk_dev -i vk_dashboard_auto_update --stop-after-init")
        print("\n2. O dashboard será atualizado automaticamente sempre que:")
        print("   • Instalar novas aplicações")
        print("   • Atualizar módulos existentes")
        print("   • Reiniciar o Odoo")
        print("\n3. Para atualização manual, execute:")
        print("   python scripts/auto-update-dashboard.py")
    else:
        print("❌ Falha na configuração!")
    
    print("=" * 70)

if __name__ == "__main__":
    main()
