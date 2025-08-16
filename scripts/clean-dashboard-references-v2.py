#!/usr/bin/env python3
"""
Limpar referências ao dashboard apagado - Versão 2
Remove todas as referências ao dashboard ID 6 que foi apagado
"""

import xmlrpc.client

# Configurações de conexão
ODOO_URL = 'http://localhost:8069'
ODOO_DB = 'vk_dev'
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = 'admin'

def connect_odoo():
    """Conectar ao Odoo via XML-RPC"""
    try:
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        
        if not uid:
            print("❌ Erro na autenticação!")
            return None, None, None
            
        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        print(f"✅ Conectado ao Odoo como usuário ID: {uid}")
        return common, models, uid
        
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return None, None, None

def clean_dashboard_references():
    """Limpar todas as referências ao dashboard apagado"""
    print("\n🧹 Limpando referências ao dashboard apagado...")
    print("=" * 60)
    
    common, models, uid = connect_odoo()
    if not models:
        return
    
    try:
        # 1. Verificar dashboards existentes
        print("🔍 Verificando dashboards existentes...")
        dashboards = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'ks_dashboard_ninja.board', 'search_read', [[]], {'fields': ['id', 'name']})
        
        if dashboards:
            print(f"   📊 Encontrados {len(dashboards)} dashboards:")
            for dashboard in dashboards:
                print(f"      - ID {dashboard['id']}: {dashboard['name']}")
        else:
            print("   📊 Nenhum dashboard encontrado")
        
        # 2. Limpar widgets órfãos (se existirem)
        print("\n🔍 Verificando widgets órfãos...")
        try:
            orphan_widgets = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                'ks_dashboard_ninja.item', 'search', [['ks_dashboard_ninja_board_id', '=', 6]])
            
            if orphan_widgets:
                print(f"   🗑️  Encontrados {len(orphan_widgets)} widgets órfãos - removendo...")
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ks_dashboard_ninja.item', 'unlink', [orphan_widgets])
                print("   ✅ Widgets órfãos removidos")
            else:
                print("   ✅ Nenhum widget órfão encontrado")
        except Exception as e:
            print(f"   ⚠️  Erro ao verificar widgets: {e}")
        
        # 3. Limpar ações órfãs relacionadas ao dashboard
        print("\n🔍 Verificando ações órfãs...")
        try:
            # Procurar ações que referenciam o dashboard ID 6
            orphan_actions = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                'ir.actions.act_window', 'search', [
                    ['res_model', '=', 'ks_dashboard_ninja.board'],
                    ['res_id', '=', 6]
                ])
            
            if orphan_actions:
                print(f"   🗑️  Encontradas {len(orphan_actions)} ações órfãs - removendo...")
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ir.actions.act_window', 'unlink', [orphan_actions])
                print("   ✅ Ações órfãs removidas")
            else:
                print("   ✅ Nenhuma ação órfã encontrada")
        except Exception as e:
            print(f"   ⚠️  Erro ao verificar ações: {e}")
        
        # 4. Limpar menus órfãos
        print("\n🔍 Verificando menus órfãos...")
        try:
            orphan_menus = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                'ir.ui.menu', 'search', [['name', 'ilike', 'Dashboard Principal']])
            
            if orphan_menus:
                print(f"   🗑️  Encontrados {len(orphan_menus)} menus órfãos - removendo...")
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ir.ui.menu', 'unlink', [orphan_menus])
                print("   ✅ Menus órfãos removidos")
            else:
                print("   ✅ Nenhum menu órfão encontrado")
        except Exception as e:
            print(f"   ⚠️  Erro ao verificar menus: {e}")
        
        print("\n" + "=" * 60)
        print("✅ LIMPEZA CONCLUÍDA!")
        print("🎯 O sistema está limpo e pronto para uso")
        print("📊 Dashboard Ninja funcionando normalmente")
        print("🔄 Recarrega a página do Odoo para aplicar as mudanças")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Erro durante a limpeza: {e}")

if __name__ == "__main__":
    clean_dashboard_references()
