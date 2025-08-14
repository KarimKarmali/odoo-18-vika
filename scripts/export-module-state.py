#!/usr/bin/env python3
"""
Exportar estado dos módulos instalados
Para sincronização Local -> CapRover
"""

import psycopg2
import json
import os
from datetime import datetime

def export_module_state():
    """Exportar lista de módulos instalados para arquivo"""
    try:
        # Conectar à database
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'vk_dev'),
            user=os.getenv('DB_USER', 'odoo'),
            password=os.getenv('DB_PASSWORD', 'odoo')
        )
        
        cur = conn.cursor()
        
        # Buscar módulos instalados
        cur.execute("""
            SELECT name, state, latest_version, auto_install, application
            FROM ir_module_module 
            WHERE state = 'installed' 
            ORDER BY name
        """)
        
        modules = []
        for name, state, version, auto_install, application in cur.fetchall():
            modules.append({
                'name': name,
                'state': state,
                'version': version,
                'auto_install': auto_install,
                'application': application
            })
        
        # Criar arquivo de estado
        state_data = {
            'exported_at': datetime.now().isoformat(),
            'database': 'vk_dev',
            'total_modules': len(modules),
            'modules': modules
        }
        
        # Salvar arquivo
        os.makedirs('config/module-states', exist_ok=True)
        
        with open('config/module-states/installed-modules.json', 'w') as f:
            json.dump(state_data, f, indent=2, default=str)
        
        print(f"✅ Estado exportado: {len(modules)} módulos")
        print(f"📁 Arquivo: config/module-states/installed-modules.json")
        
        # Mostrar módulos importantes
        important = ['sale', 'sale_management', 'purchase', 'account']
        print(f"\n📋 MÓDULOS IMPORTANTES:")
        for module in modules:
            if module['name'] in important:
                print(f"  ✅ {module['name']}")
        
        cur.close()
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    print("🔄 Exportando estado dos módulos...")
    export_module_state()
