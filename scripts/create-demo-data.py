#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para criar dados dummy para testar SAF-T
Execute no container Odoo ou via odoo shell
"""

import datetime

def create_dummy_data(env):
    """Criar dados dummy para SAF-T"""
    print("🏗️  Criando dados dummy para SAF-T...")
    
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
    customers_data = [
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
    
    customers = []
    for customer_data in customers_data:
        customer = env['res.partner'].create(customer_data)
        customers.append(customer)
        print(f"     ✅ Cliente criado: {customer.name}")
    
    # 3. Criar fornecedores dummy
    print("   🏪 Criando fornecedores dummy...")
    suppliers_data = [
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
    
    suppliers = []
    for supplier_data in suppliers_data:
        supplier = env['res.partner'].create(supplier_data)
        suppliers.append(supplier)
        print(f"     ✅ Fornecedor criado: {supplier.name}")
        
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
        print("     ✅ IVA 23% criado")
    else:
        iva_23.write({
            'saft_tax_type': 'IVA',
            'saft_tax_code': 'NOR',
            'saft_country_region': 'PT',
        })
        print("     ✅ IVA 23% configurado")
    
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
        print("     ✅ IVA 6% criado")
    else:
        iva_6.write({
            'saft_tax_type': 'IVA',
            'saft_tax_code': 'RED',
            'saft_country_region': 'PT',
        })
        print("     ✅ IVA 6% configurado")
    
    # 5. Criar produtos dummy
    print("   📦 Criando produtos dummy...")
    products_data = [
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
    
    products = []
    for product_data in products_data:
        product = env['product.product'].create(product_data)
        products.append(product)
        print(f"     ✅ Produto criado: {product.name}")
    
    # 6. Criar faturas dummy para agosto 2024
    print("   🧾 Criando faturas dummy...")
    
    for i, customer in enumerate(customers):
        # Fatura
        invoice_date = datetime.date(2024, 8, 5 + i*3)
        
        invoice = env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': customer.id,
            'invoice_date': invoice_date,
            'invoice_line_ids': [
                (0, 0, {
                    'product_id': products[i % len(products)].id,
                    'quantity': 2 + i,
                    'price_unit': products[i % len(products)].list_price,
                    'tax_ids': products[i % len(products)].taxes_id.ids,
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
    
    print("✅ Dados dummy criados com sucesso!")
    print("")
    print("📋 Resumo dos dados criados:")
    print(f"   • Empresa: VK Commodities Demo (NIF: PT123456789)")
    print(f"   • Clientes: {len(customers)} criados")
    print(f"   • Fornecedores: {len(suppliers)} criados")
    print(f"   • Produtos: {len(products)} criados")
    print(f"   • Impostos: IVA 23% e IVA 6% configurados")
    print(f"   • Faturas: {len(customers)} faturas de agosto 2024")
    print(f"   • Movimentos: Movimentos contabilísticos de teste")
    print("")
    
    return True

# Para usar no odoo shell:
# env['ir.module.module'].search([('name', '=', 'l10n_pt_saft')]).button_immediate_install()
# exec(open('scripts/create-demo-data.py').read())
# create_dummy_data(env)
