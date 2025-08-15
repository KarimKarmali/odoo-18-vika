# Script para instalar módulo SAF-T e criar dados dummy
# Encoding: UTF-8

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   🇵🇹 INSTALAÇÃO SAF-T + DADOS DUMMY   " -ForegroundColor Cyan  
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se Docker está rodando
Write-Host "1. Verificando Docker..." -ForegroundColor Yellow
try {
    $dockerStatus = docker info 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Docker está rodando" -ForegroundColor Green
    } else {
        Write-Host "   ❌ Docker não está rodando" -ForegroundColor Red
        Write-Host "   Por favor, inicie o Docker Desktop primeiro" -ForegroundColor Red
        exit 1
    }
} catch {
    Write-Host "   ❌ Docker não encontrado" -ForegroundColor Red
    exit 1
}

# Verificar se containers estão ativos
Write-Host "2. Verificando containers..." -ForegroundColor Yellow
$containers = docker-compose ps --services --filter "status=running" 2>$null
if ($containers -match "odoo") {
    Write-Host "   ✅ Odoo container ativo" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Iniciando containers..." -ForegroundColor Yellow
    docker-compose up -d
    Start-Sleep 10
}

# Criar dados dummy via Python script
Write-Host "3. Criando dados dummy..." -ForegroundColor Yellow

$pythonScript = @"
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import datetime

# Configurar ambiente Odoo
sys.path.append('/opt/odoo/odoo')
sys.path.append('/opt/odoo/addons/custom')
sys.path.append('/opt/odoo/addons/oca')

os.environ['ODOO_RC'] = '/opt/odoo/config/odoo.conf'

import odoo
from odoo import api, SUPERUSER_ID

def create_dummy_data():
    print("🏗️  Criando dados dummy para SAF-T...")
    
    # Conectar à base de dados
    db_name = 'odoo'
    
    try:
        # Registrar base de dados se necessário
        if db_name not in odoo.service.db.list_dbs():
            print(f"❌ Base de dados '{db_name}' não encontrada")
            return False
            
        # Conectar
        with api.Environment.manage():
            env = api.Environment(odoo.registry(db_name), SUPERUSER_ID, {})
            
            # 1. Configurar empresa
            print("   📋 Configurando empresa...")
            company = env['res.company'].browse(1)
            company.write({
                'name': 'VK Commodities Demo',
                'vat': 'PT123456789',
                'street': 'Rua de Exemplo, 123',
                'city': 'Lisboa',
                'zip': '1000-001',
                'country_id': env.ref('base.pt').id,
                'saft_legal_form': 'Lda',
                'saft_company_registration_number': '123456789',
            })
            
            # 2. Criar clientes dummy
            print("   👥 Criando clientes dummy...")
            customers = [
                {
                    'name': 'Cliente Demo 1',
                    'vat': 'PT987654321',
                    'street': 'Av. Cliente 1, 456',
                    'city': 'Porto',
                    'zip': '4000-001',
                    'country_id': env.ref('base.pt').id,
                    'customer_rank': 1,
                    'is_company': True,
                },
                {
                    'name': 'Cliente Demo 2',
                    'vat': 'PT111222333',
                    'street': 'Rua Cliente 2, 789',
                    'city': 'Braga',
                    'zip': '4700-001',
                    'country_id': env.ref('base.pt').id,
                    'customer_rank': 1,
                    'is_company': True,
                }
            ]
            
            for customer_data in customers:
                env['res.partner'].create(customer_data)
            
            # 3. Criar fornecedores dummy
            print("   🏪 Criando fornecedores dummy...")
            suppliers = [
                {
                    'name': 'Fornecedor Demo 1',
                    'vat': 'PT444555666',
                    'street': 'Rua Fornecedor 1, 101',
                    'city': 'Coimbra',
                    'zip': '3000-001',
                    'country_id': env.ref('base.pt').id,
                    'supplier_rank': 1,
                    'is_company': True,
                },
                {
                    'name': 'Fornecedor Demo 2', 
                    'vat': 'PT777888999',
                    'street': 'Av. Fornecedor 2, 202',
                    'city': 'Faro',
                    'zip': '8000-001',
                    'country_id': env.ref('base.pt').id,
                    'supplier_rank': 1,
                    'is_company': True,
                }
            ]
            
            for supplier_data in suppliers:
                env['res.partner'].create(supplier_data)
                
            # 4. Configurar impostos portugueses
            print("   💰 Configurando impostos...")
            
            # IVA 23%
            iva_23 = env['account.tax'].search([
                ('company_id', '=', company.id),
                ('amount', '=', 23.0),
                ('type_tax_use', '=', 'sale')
            ], limit=1)
            
            if not iva_23:
                iva_23 = env['account.tax'].create({
                    'name': 'IVA 23%',
                    'amount': 23.0,
                    'type_tax_use': 'sale',
                    'company_id': company.id,
                    'saft_tax_type': 'IVA',
                    'saft_tax_code': 'NOR',
                    'saft_country_region': 'PT',
                })
            else:
                iva_23.write({
                    'saft_tax_type': 'IVA',
                    'saft_tax_code': 'NOR',
                    'saft_country_region': 'PT',
                })
            
            # IVA 6%
            iva_6 = env['account.tax'].search([
                ('company_id', '=', company.id),
                ('amount', '=', 6.0),
                ('type_tax_use', '=', 'sale')
            ], limit=1)
            
            if not iva_6:
                iva_6 = env['account.tax'].create({
                    'name': 'IVA 6%',
                    'amount': 6.0,
                    'type_tax_use': 'sale',
                    'company_id': company.id,
                    'saft_tax_type': 'IVA',
                    'saft_tax_code': 'RED',
                    'saft_country_region': 'PT',
                })
            else:
                iva_6.write({
                    'saft_tax_type': 'IVA',
                    'saft_tax_code': 'RED',
                    'saft_country_region': 'PT',
                })
            
            # 5. Criar produtos dummy
            print("   📦 Criando produtos dummy...")
            products = [
                {
                    'name': 'Produto Demo 1',
                    'default_code': 'PROD001',
                    'list_price': 100.0,
                    'taxes_id': [(6, 0, [iva_23.id])],
                    'type': 'product',
                },
                {
                    'name': 'Produto Demo 2',
                    'default_code': 'PROD002', 
                    'list_price': 50.0,
                    'taxes_id': [(6, 0, [iva_6.id])],
                    'type': 'product',
                },
                {
                    'name': 'Serviço Demo 1',
                    'default_code': 'SERV001',
                    'list_price': 200.0,
                    'taxes_id': [(6, 0, [iva_23.id])],
                    'type': 'service',
                }
            ]
            
            created_products = []
            for product_data in products:
                product = env['product.product'].create(product_data)
                created_products.append(product)
            
            # 6. Criar faturas dummy para agosto 2024
            print("   🧾 Criando faturas dummy...")
            
            customers_list = env['res.partner'].search([('customer_rank', '>', 0)], limit=2)
            
            if customers_list:
                for i, customer in enumerate(customers_list):
                    # Fatura 1
                    invoice_date = datetime.date(2024, 8, 5 + i*3)
                    
                    invoice = env['account.move'].create({
                        'move_type': 'out_invoice',
                        'partner_id': customer.id,
                        'invoice_date': invoice_date,
                        'invoice_line_ids': [
                            (0, 0, {
                                'product_id': created_products[i % len(created_products)].id,
                                'quantity': 2 + i,
                                'price_unit': created_products[i % len(created_products)].list_price,
                                'tax_ids': created_products[i % len(created_products)].taxes_id.ids,
                            })
                        ]
                    })
                    
                    # Validar fatura
                    invoice.action_post()
                    
                    print(f"     ✅ Fatura {invoice.name} criada para {customer.name}")
            
            # 7. Criar movimentos contabilísticos dummy
            print("   📊 Criando movimentos contabilísticos...")
            
            # Movimento de caixa
            cash_journal = env['account.journal'].search([
                ('type', '=', 'cash'),
                ('company_id', '=', company.id)
            ], limit=1)
            
            if cash_journal:
                cash_account = cash_journal.default_account_id
                expense_account = env['account.account'].search([
                    ('account_type', '=', 'expense'),
                    ('company_id', '=', company.id)
                ], limit=1)
                
                if cash_account and expense_account:
                    move = env['account.move'].create({
                        'journal_id': cash_journal.id,
                        'date': datetime.date(2024, 8, 15),
                        'ref': 'Movimento Dummy - Despesa de Escritório',
                        'line_ids': [
                            (0, 0, {
                                'account_id': expense_account.id,
                                'name': 'Despesa de Escritório',
                                'debit': 150.0,
                                'credit': 0.0,
                            }),
                            (0, 0, {
                                'account_id': cash_account.id,
                                'name': 'Pagamento em Dinheiro',
                                'debit': 0.0,
                                'credit': 150.0,
                            })
                        ]
                    })
                    
                    move.action_post()
                    print(f"     ✅ Movimento {move.name} criado")
            
            env.cr.commit()
            
            print("✅ Dados dummy criados com sucesso!")
            print("")
            print("📋 Resumo dos dados criados:")
            print(f"   • Empresa: VK Commodities Demo (NIF: PT123456789)")
            print(f"   • Clientes: {len(customers)} criados")
            print(f"   • Fornecedores: {len(suppliers)} criados")
            print(f"   • Produtos: {len(products)} criados")
            print(f"   • Impostos: IVA 23% e IVA 6% configurados")
            print(f"   • Faturas: Várias faturas de agosto 2024")
            print(f"   • Movimentos: Movimentos contabilísticos de teste")
            print("")
            
            return True
            
    except Exception as e:
        print(f"❌ Erro ao criar dados dummy: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    create_dummy_data()
"@

# Escrever script Python temporário
$tempScript = "temp_create_dummy.py"
$pythonScript | Out-File -FilePath $tempScript -Encoding UTF8

# Executar script dentro do container
Write-Host "   🐍 Executando script Python..." -ForegroundColor Yellow
try {
    docker-compose exec -T odoo python3 /opt/odoo/$tempScript
    if ($LASTEXITCODE -eq 0) {
        Write-Host "   ✅ Dados dummy criados!" -ForegroundColor Green
    } else {
        Write-Host "   ❌ Erro ao criar dados" -ForegroundColor Red
    }
} catch {
    Write-Host "   ❌ Erro na execução: $_" -ForegroundColor Red
}

# Limpar arquivo temporário
Remove-Item $tempScript -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "4. Testando acesso ao SAF-T..." -ForegroundColor Yellow
Write-Host ""
Write-Host "📋 Para testar o módulo SAF-T:" -ForegroundColor White
Write-Host "   1. Abra http://localhost:8069" -ForegroundColor White
Write-Host "   2. Apps - Update Apps List" -ForegroundColor White
Write-Host "   3. Procure 'SAF-T Portugal'" -ForegroundColor White
Write-Host "   4. Clique em Install" -ForegroundColor White
Write-Host "   5. Accounting - Reporting - SAF-T Export" -ForegroundColor White
Write-Host ""
Write-Host "📅 Período de teste:" -ForegroundColor White
Write-Host "   • Start Date: 01/08/2024" -ForegroundColor White
Write-Host "   • End Date: 31/08/2024" -ForegroundColor White
Write-Host "   • Type: Both" -ForegroundColor White
Write-Host ""
Write-Host "✅ Pronto para testar SAF-T!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
