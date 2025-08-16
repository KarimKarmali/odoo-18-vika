#!/usr/bin/env python3
"""
Corrigir Ação Padrão do Odoo
Define a página inicial correta (não a configuração do dashboard)
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

def fix_default_action():
    """Corrigir a ação padrão para mostrar a página inicial normal do Odoo"""
    print("\n🔧 Corrigindo Ação Padrão do Odoo...")
    print("=" * 60)
    
    common, models, uid = connect_odoo()
    if not models:
        return
    
    try:
        # 1. Verificar a ação atual 589
        print("🔍 Verificando ação 589...")
        action_589 = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
            'ir.actions.act_window', 'search_read', [[['id', '=', 589]]], 
            {'fields': ['id', 'name', 'res_model', 'res_id', 'view_mode']})
        
        if action_589:
            action = action_589[0]
            print(f"   📋 Ação 589: {action['name']}")
            print(f"   📋 Modelo: {action.get('res_model', 'N/A')}")
            print(f"   📋 Res ID: {action.get('res_id', 'N/A')}")
            print(f"   📋 View Mode: {action.get('view_mode', 'N/A')}")
        
        # 2. Opção 1: Remover a ação padrão (deixar Odoo usar a página inicial normal)
        print("\n🏠 Removendo ação padrão personalizada...")
        try:
            # Procurar por uma ação de "Apps" ou "Home" padrão do Odoo
            home_actions = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                'ir.actions.act_window', 'search_read', [
                    ['|', ['name', 'ilike', 'Apps'], ['name', 'ilike', 'Home']]
                ], {'fields': ['id', 'name', 'res_model'], 'limit': 5})
            
            if home_actions:
                print("   📱 Ações disponíveis:")
                for action in home_actions:
                    print(f"      - ID {action['id']}: {action['name']} ({action.get('res_model', 'N/A')})")
                
                # Usar a primeira ação encontrada
                default_action = home_actions[0]
                print(f"\n   🎯 Definindo ação padrão: {default_action['name']}")
                
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ir.actions.act_window', 'write', [[589], {
                        'name': default_action['name'],
                        'res_model': default_action.get('res_model', 'ir.module.module'),
                        'res_id': False,
                        'view_mode': 'kanban,tree,form'
                    }])
                print("   ✅ Ação padrão atualizada")
            else:
                # Se não encontrar, definir para a página de Apps
                print("   📱 Definindo para página de Apps...")
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ir.actions.act_window', 'write', [[589], {
                        'name': 'Apps',
                        'res_model': 'ir.module.module',
                        'res_id': False,
                        'view_mode': 'kanban,tree,form',
                        'domain': "[('state','=','installed'),('application','=',True)]"
                    }])
                print("   ✅ Ação definida para página de Apps")
                
        except Exception as e:
            print(f"   ⚠️  Erro ao definir ação padrão: {str(e)[:100]}...")
        
        # 3. Opção alternativa: Remover completamente a ação personalizada
        print("\n🗑️  Opção alternativa: Remover ação personalizada...")
        try:
            # Verificar se existe uma ação padrão do sistema
            system_actions = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                'ir.actions.act_window', 'search_read', [
                    [('res_model', '=', 'ir.module.module'), ('name', '=', 'Apps')]
                ], {'fields': ['id', 'name'], 'limit': 1})
            
            if system_actions:
                system_action = system_actions[0]
                print(f"   🎯 Ação do sistema encontrada: ID {system_action['id']}")
                
                # Apagar a ação 589 personalizada
                models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
                    'ir.actions.act_window', 'unlink', [[589]])
                print("   ✅ Ação personalizada removida - Odoo usará a página inicial padrão")
            else:
                print("   ⚠️  Mantendo ação atual como fallback")
                
        except Exception as e:
            print(f"   ⚠️  Erro ao remover ação: {str(e)[:100]}...")
        
        print("\n" + "=" * 60)
        print("✅ CORREÇÃO DA AÇÃO PADRÃO CONCLUÍDA!")
        print("🏠 Agora o Odoo deve mostrar a página inicial normal")
        print("🔄 RECARREGA A PÁGINA DO ODOO PARA VER A MUDANÇA!")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Erro durante a correção: {e}")

if __name__ == "__main__":
    fix_default_action()
