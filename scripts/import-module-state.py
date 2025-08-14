#!/usr/bin/env python3
"""
Importar e aplicar estado dos módulos
Para uso no CapRover após deploy
"""

import json
import os
import subprocess
import sys

def install_modules_from_state():
    """Instalar módulos baseado no arquivo de estado"""
    
    state_file = 'config/module-states/installed-modules.json'
    
    if not os.path.exists(state_file):
        print("❌ Arquivo de estado não encontrado!")
        return False
    
    try:
        with open(state_file, 'r') as f:
            state_data = json.load(f)
        
        modules = state_data.get('modules', [])
        total = len(modules)
        
        print(f"📋 Estado exportado em: {state_data.get('exported_at', 'N/A')}")
        print(f"🔢 Total de módulos: {total}")
        
        # Filtrar apenas módulos que devem ser instalados
        install_list = []
        for module in modules:
            name = module['name']
            state = module['state']
            
            # Pular módulos base que são instalados automaticamente
            if name in ['base', 'web']:
                continue
                
            if state == 'installed':
                install_list.append(name)
        
        if not install_list:
            print("ℹ️ Nenhum módulo para instalar")
            return True
        
        print(f"📦 Módulos a instalar: {len(install_list)}")
        
        # Criar comando de instalação
        modules_str = ','.join(install_list)
        
        print(f"🔧 Comando que deve ser executado:")
        print(f"odoo -i {modules_str} --stop-after-init")
        
        # Para CapRover, apenas mostrar o comando
        # O comando real seria executado pelo container
        print("\n" + "="*50)
        print("INSTRUÇÕES PARA CAPROVER:")
        print("="*50)
        print("1. Após deploy, execute no container:")
        print(f"   odoo -i {modules_str} --stop-after-init")
        print("2. Depois reinicie normalmente:")
        print("   odoo")
        print("="*50)
        
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Importando estado dos módulos...")
    install_modules_from_state()
