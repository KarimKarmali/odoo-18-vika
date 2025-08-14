#!/usr/bin/env python3
"""
Script de Infrastructure as Code para Odoo 18
VK Commodities - Setup automático de produção
"""

import psycopg2
import sys
import os

# Configuração de módulos obrigatórios
REQUIRED_MODULES = [
    'sale_management',
    'purchase',
    'stock', 
    'account_accountant',
    'project',
    'hr',
    'crm',
    'website'
]

# Configuração da empresa
COMPANY_CONFIG = {
    'name': 'VK Commodities',
    'currency': 'EUR',
    'country': 'Portugal',
    'timezone': 'Europe/Lisbon'
}

def install_modules(modules_list):
    """Instalar módulos via código (não interface)"""
    print(f"🔧 Instalando {len(modules_list)} módulos...")
    
    try:
        # Conectar à database
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'vk_dev'),
            user=os.getenv('DB_USER', 'odoo'),
            password=os.getenv('DB_PASSWORD', 'odoo')
        )
        
        cur = conn.cursor()
        
        # Marcar módulos para instalação
        for module in modules_list:
            cur.execute("""
                UPDATE ir_module_module 
                SET state = 'to install' 
                WHERE name = %s AND state = 'uninstalled'
            """, (module,))
            print(f"  ✅ {module} marcado para instalação")
        
        conn.commit()
        cur.close()
        conn.close()
        
        print("✅ Módulos marcados! Execute Odoo com -u all para aplicar")
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

def configure_company():
    """Configurar empresa automaticamente"""
    print("🏢 Configurando empresa...")
    # Este seria executado após instalação dos módulos
    pass

def main():
    """Setup completo de produção"""
    print("=" * 50)
    print("🚀 SETUP PRODUÇÃO - VK COMMODITIES")
    print("=" * 50)
    
    # 1. Instalar módulos obrigatórios
    if install_modules(REQUIRED_MODULES):
        print("\n✅ Setup concluído!")
        print("🔄 Execute: odoo -u all para aplicar mudanças")
    else:
        print("\n❌ Setup falhou!")
        sys.exit(1)

if __name__ == "__main__":
    main()
