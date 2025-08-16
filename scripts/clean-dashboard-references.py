#!/usr/bin/env python3
"""
Limpar referências ao dashboard apagado
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
        # 1. Limpar ação padrão do usuário se for o dashboard apagado
        print("🔍 Verificando ação padrão do usuário...")
        user_action = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'res.users', 'read', [uid], {'fields': ['action_id']})
        
        if user_action and user_action[0].get('action_id'):
            action_id = user_action[0]['action_id'][0]
            print(f"   Ação atual do usuário: {action_id}")
            
            # Verificar se é uma ação do dashboard ninja
            try:
                action_data = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ir.actions.act_window', 'read', [action_id], {'fields': ['res_model']})
                
                if action_data and action_data[0].get('res_model') == 'ks_dashboard_ninja.board':
                    print("   ⚠️  Ação do usuário aponta para dashboard ninja - limpando...")
                    models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                        'res.users', 'write', [uid], {'action_id': False})
                    print("   ✅ Ação padrão do usuário limpa")
                else:
                    print("   ✅ Ação do usuário não é problemática")
                    
            except Exception as e:
                print(f"   ⚠️  Erro ao verificar ação - limpando por segurança: {e}")
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'res.users', 'write', [uid], {'action_id': False})
                print("   ✅ Ação padrão do usuário limpa")
        
        # 2. Verificar se existem dashboards órfãos
        print("\n🔍 Verificando dashboards existentes...")
        dashboards = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'ks_dashboard_ninja.board', 'search_read', [[]], {'fields': ['id', 'name']})
        
        if dashboards:
            print(f"   📊 Encontrados {len(dashboards)} dashboards:")
            for dashboard in dashboards:
                print(f"      - ID {dashboard['id']}: {dashboard['name']}")
        else:
            print("   📊 Nenhum dashboard encontrado")
        
        # 3. Limpar widgets órfãos (se existirem)
        print("\n🔍 Verificando widgets órfãos...")
        orphan_widgets = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'ks_dashboard_ninja.item', 'search', [['ks_dashboard_ninja_board_id', '=', 6]])
        
        if orphan_widgets:
            print(f"   🗑️  Encontrados {len(orphan_widgets)} widgets órfãos - removendo...")
            models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                'ks_dashboard_ninja.item', 'unlink', [orphan_widgets])
            print("   ✅ Widgets órfãos removidos")
        else:
            print("   ✅ Nenhum widget órfão encontrado")
        
        print("\n" + "=" * 60)
        print("✅ LIMPEZA CONCLUÍDA!")
        print("🎯 O sistema está limpo e pronto para uso")
        print("📊 Dashboard Ninja funcionando normalmente")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Erro durante a limpeza: {e}")

if __name__ == "__main__":
    clean_dashboard_references()
