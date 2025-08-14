#!/usr/bin/env python3
"""
Script para instalar mis_builder manualmente
VK Commodities
"""

import odoo
from odoo import api, SUPERUSER_ID

def install_mis_builder():
    """Instala o módulo mis_builder forçadamente"""
    
    # Configurar Odoo
    odoo.tools.config.parse_config(['-c', '/etc/odoo/odoo.conf'])
    
    # Conectar à database
    db_name = 'vk_dev'  # ou o nome da sua database
    
    with api.Environment.manage():
        with odoo.registry(db_name).cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            # Atualizar lista de módulos
            print("🔄 Atualizando lista de módulos...")
            env['ir.module.module'].update_list()
            
            # Procurar módulo mis_builder
            module = env['ir.module.module'].search([('name', '=', 'mis_builder')])
            
            if not module:
                print("❌ Módulo mis_builder não encontrado na lista!")
                return False
                
            print(f"✅ Módulo encontrado: {module.name} - Estado: {module.state}")
            
            # Verificar dependências
            print("🔍 Verificando dependências...")
            dependencies = ['account', 'board', 'report_xlsx', 'date_range']
            
            for dep in dependencies:
                dep_module = env['ir.module.module'].search([
                    ('name', '=', dep),
                    ('state', '=', 'installed')
                ])
                if dep_module:
                    print(f"  ✅ {dep}")
                else:
                    print(f"  ❌ {dep} - NÃO INSTALADO")
                    # Tentar instalar dependência
                    dep_to_install = env['ir.module.module'].search([('name', '=', dep)])
                    if dep_to_install:
                        print(f"  🔄 Instalando {dep}...")
                        dep_to_install.button_immediate_install()
            
            # Instalar mis_builder
            if module.state != 'installed':
                print("🚀 Instalando mis_builder...")
                module.button_immediate_install()
                print("✅ mis_builder instalado com sucesso!")
            else:
                print("ℹ️ mis_builder já está instalado")
            
            return True

if __name__ == '__main__':
    install_mis_builder()
