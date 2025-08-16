#!/usr/bin/env python3
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
            print("\n📋 Próximos passos:")
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
