# Módulo de Contabilidade VK Commodities
## Sistema Completo de Gestão Financeira para Portugal

![Versão](https://img.shields.io/badge/version-18.0.1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-Production-green.svg)
![Licença](https://img.shields.io/badge/license-LGPL--3-blue.svg)

---

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Módulos de Contabilidade](#módulos-de-contabilidade)
3. [Configuração por Módulo](#configuração-por-módulo)
4. [Localização Portuguesa](#localização-portuguesa)
5. [InvoiceXpress Integration](#invoicexpress-integration)
6. [Plano de Contas Português](#plano-de-contas-português)
7. [IVA e Códigos de Isenção](#iva-e-códigos-de-isenção)
8. [Mapas de IVA](#mapas-de-iva)
9. [SAF-T (AT)](#saf-t-at)
10. [Guias de Transporte](#guias-de-transporte)
11. [Relatórios Contabilísticos](#relatórios-contabilísticos)
12. [Centros de Custo](#centros-de-custo)
13. [Contabilidade Analítica](#contabilidade-analítica)
14. [Troubleshooting](#troubleshooting)

---

## 🎯 Visão Geral

O **Módulo de Contabilidade VK Commodities** é uma solução completa de gestão financeira adaptada às especificidades legais e fiscais portuguesas. Integra todos os processos contabilísticos desde vendas até relatórios oficiais.

### Características Principais:
- ✅ **Conformidade Legal**: 100% adequado à legislação portuguesa
- ✅ **Integração InvoiceXpress**: Faturação automática
- ✅ **SAF-T Automático**: Geração e envio para AT
- ✅ **Plano de Contas SNC**: Pré-configurado
- ✅ **IVA Automático**: Cálculo e mapas
- ✅ **Relatórios Legais**: Balancetes, DRE, etc.

---

## 📊 Módulos de Contabilidade

### 1. Sales Management (Vendas)
**Módulo**: `sale_management`

#### Funcionalidades:
- **Orçamentos**: Criação e conversão em vendas
- **Encomendas**: Gestão do pipeline de vendas
- **Faturação**: Integração automática com contabilidade
- **Comissões**: Cálculo automático para comerciais

#### Como Funciona:
```
Orçamento → Encomenda → Guia de Remessa → Fatura → Lançamento Contabilístico
```

#### Integração Contabilística:
- Criação automática de movimentos no razão
- Reconhecimento de receita
- Controlo de crédito automático
- IVA calculado automaticamente

---

### 2. Purchase Management (Compras)
**Módulo**: `purchase`

#### Funcionalidades:
- **Pedidos de Cotação**: Comparação de fornecedores
- **Encomendas de Compra**: Gestão de aprovações
- **Receção**: Controlo de mercadorias
- **Faturação de Fornecedores**: Validação automática

#### Fluxo de Trabalho:
```
RFQ → Purchase Order → Receipt → Vendor Bill → Payment
```

#### Controlos Automáticos:
- Validação de preços vs. encomenda
- Controlo de orçamentos
- Aprovações por hierarquia
- Lançamentos automáticos em fornecedores

---

### 3. Inventory Management (Inventário)
**Módulo**: `stock`

#### Funcionalidades Core:
- **Multi-Armazém**: Gestão de várias localizações
- **Rastreabilidade**: Lotes e números de série
- **Valorização**: FIFO, LIFO, Custo Médio
- **Inventários**: Cíclicos e anuais

#### Valorização de Stock:
```python
# Configuração de Valorização
Produto > Contabilidade > Valorização: 
- Custo Médio (Recomendado)
- FIFO (Primeiro a Entrar, Primeiro a Sair)
- Standard Price (Preço Fixo)
```

#### Integração Contabilística:
- Movimentos automáticos de stock
- Provisões para obsolescência
- Ajustes de inventário
- Custo das vendas automático

---

### 4. Invoicing (Faturação)
**Módulo**: `account`

#### Tipos de Documentos:
- **Faturas**: FT, FR, FS
- **Notas de Crédito**: NC
- **Notas de Débito**: ND
- **Recibos**: RC
- **Guias**: GT, GR, GC

#### Numeração Portuguesa:
```
Série/Ano/Número Sequencial
Exemplo: FT/2024/000001
```

#### Validações Automáticas:
- NIF português válido
- Códigos de IVA corretos
- Campos obrigatórios AT
- Hash codes (ATCUD)

---

### 5. Accounting (Contabilidade)
**Módulo**: `account_accountant`

#### Módulos Avançados:
- **Reconciliação Bancária**: Automática
- **Multi-Currency**: Gestão de câmbios
- **Consolidação**: Multi-empresas
- **Budget Control**: Controlo orçamental
- **Asset Management**: Imobilizado

---

## ⚙️ Configuração por Módulo

### Sales Configuration

#### 1. Configurações Básicas
```
Sales > Configuration > Settings:
✅ Quotations & Orders
✅ Invoicing Policy: Delivered quantities
✅ Customer Portal
✅ Sales Teams
```

#### 2. Condições de Pagamento
```sql
-- Criação via SQL para automação
INSERT INTO account_payment_term (name, company_id) VALUES 
('Pronto Pagamento', 1),
('30 dias', 1),
('60 dias', 1);
```

#### 3. Termos de Entrega (Incoterms)
```
Inventory > Configuration > Delivery Terms
- EXW (Ex Works)
- FCA (Free Carrier) 
- DAP (Delivered at Place)
- DDP (Delivered Duty Paid)
```

### Purchase Configuration

#### 1. Aprovações
```
Purchase > Configuration > Settings:
✅ Purchase Order Approval
✅ 3-way matching (PO/Receipt/Vendor Bill)
✅ Lock confirmed orders
```

#### 2. Categorias de Compra
```python
# Configuração automática
categories = [
    'Matérias Primas',
    'Mercadorias',
    'Serviços',
    'Ativos Fixos'
]
```

### Inventory Configuration

#### 1. Armazéns e Localizações
```
Configuração Recomendada:
├── Armazém Principal
│   ├── Receção
│   ├── Stock
│   ├── Expedição
│   └── Controlo Qualidade
└── Armazém Trânsito
    ├── Clientes
    └── Fornecedores
```

#### 2. Operações de Stock
```
Inventory > Configuration > Operations:
- Receções: 2 steps (Input + Stock)
- Entregas: 2 steps (Pick + Ship)
- Fabricação: se aplicável
```

---

## 🇵🇹 Localização Portuguesa

### Módulos Específicos Portugal

#### 1. l10n_pt_vat
**Funcionalidades:**
- Validação de NIF português
- Códigos de IVA específicos
- Códigos de isenção AT
- Validação VIES (UE)

#### 2. l10n_pt_account_invoicexpress
**Integração completa com InvoiceXpress**

#### 3. l10n_pt_stock_invoicexpress
**Documentos de transporte automáticos**

### Configuração Base Portugal
```python
# Company Settings
company_data = {
    'name': 'VK Commodities',
    'country_id': 'Portugal',
    'currency_id': 'EUR',
    'vat': 'PT123456789',
    'phone': '+351 XXX XXX XXX'
}
```

---

## 📱 InvoiceXpress Integration

### O que é o InvoiceXpress?
Software de faturação certificado pela AT (Autoridade Tributária) que permite:
- Faturação legal portuguesa
- Comunicação automática à AT
- Arquivo digital legal
- QR Codes obrigatórios

### Como Está Integrado

#### 1. Configuração Inicial
```
Accounting > Configuration > InvoiceXpress:
- API Key: [Sua chave API]
- Account Name: [Nome da conta]
- Environment: Production/Sandbox
```

#### 2. Mapeamento de Documentos
```python
# Mapeamento automático
odoo_to_ix = {
    'out_invoice': 'Invoice',
    'out_refund': 'CreditNote', 
    'in_invoice': 'PurchaseInvoice',
    'out_receipt': 'Receipt'
}
```

#### 3. Processo Automático
```
1. Fatura criada no Odoo
2. Validação dos dados
3. Envio para InvoiceXpress
4. Receção do PDF legal
5. Anexo automático no Odoo
6. Comunicação AT (se configurado)
```

### O que Altera no Processo
- **Antes**: Fatura manual → Envio manual AT
- **Depois**: Fatura Odoo → Automático InvoiceXpress → Automático AT

### Benefícios:
- ✅ Conformidade legal garantida
- ✅ Redução de erros
- ✅ Processo 100% automático
- ✅ Arquivo digital organizado

---

## 💼 Plano de Contas Português

### Sistema de Normalização Contabilística (SNC)

#### Estrutura Base:
```
Classe 1 - Meios Financeiros Líquidos
├── 11 - Caixa
├── 12 - Depósitos bancários
├── 13 - Outros depósitos bancários
└── 14 - Outros instrumentos financeiros

Classe 2 - Contas a Receber e a Pagar
├── 21 - Clientes
├── 22 - Fornecedores
├── 23 - Estado e outros entes públicos
└── 24 - Outros devedores e credores

Classe 3 - Inventários e Ativos Biológicos
├── 31 - Compras
├── 32 - Mercadorias
├── 33 - Matérias-primas
└── 35 - Produtos acabados

Classe 4 - Capital, Reservas e Resultados
├── 41 - Capital realizado
├── 42 - Ações/quotas próprias
├── 43 - Reservas legais
└── 44 - Reservas livres

Classe 5 - Capital e Ativos Fixos Tangíveis
├── 51 - Ativos fixos tangíveis
├── 52 - Ativos fixos intangíveis
└── 53 - Ativos de direito de uso

Classe 6 - Gastos
├── 61 - Custo das mercadorias vendidas
├── 62 - Fornecimentos e serviços externos
├── 63 - Gastos com pessoal
└── 64 - Gastos de depreciação

Classe 7 - Rendimentos
├── 71 - Vendas
├── 72 - Prestações de serviços
└── 73 - Proveitos suplementares

Classe 8 - Resultados
├── 81 - Resultados líquidos do período
└── 88 - Resultado líquido do exercício
```

### Configuração Automática
```python
# Script de instalação do plano de contas
def install_portuguese_chart():
    # Criação automática baseada no SNC
    accounts = load_from_file('l10n_pt_chart.xml')
    create_account_hierarchy(accounts)
```

---

## 🧾 IVA e Códigos de Isenção

### Taxas de IVA em Portugal (2024)

#### Taxa Normal: 23%
```python
# Configuração no Odoo
vat_23 = {
    'name': 'IVA 23%',
    'type_tax_use': 'sale',
    'amount': 23.0,
    'account_id': account_233000  # IVA Liquidado
}
```

#### Taxa Intermédia: 13%
```python
vat_13 = {
    'name': 'IVA 13%',
    'type_tax_use': 'sale', 
    'amount': 13.0,
    'account_id': account_233000
}
```

#### Taxa Reduzida: 6%
```python
vat_6 = {
    'name': 'IVA 6%',
    'type_tax_use': 'sale',
    'amount': 6.0, 
    'account_id': account_233000
}
```

### Códigos de Isenção Portuguesa

#### Principais Códigos AT:
```python
exemption_codes = {
    'M01': 'Artigo 16.º n.º 6 alínea c) do CIVA',
    'M02': 'Artigo 6.º do Decreto-Lei n.º 198/90',
    'M03': 'Exigibilidade de caixa',
    'M04': 'Regime especial viajantes',
    'M05': 'Regime especial agências viagem', 
    'M06': 'Regime especial bens em segunda mão',
    'M07': 'Regime especial obras de arte',
    'M08': 'Regime especial objetos coleção',
    'M09': 'Regime especial objetos antiguidade',
    'M10': 'Regime especial tabaco',
    'M11': 'Regime especial jornais e revistas',
    'M12': 'Triangulação',
    'M13': 'Autoliquidação',
    'M14': 'Outras situações'
}
```

#### Configuração no Odoo:
```python
# Criação de impostos isentos
for code, description in exemption_codes.items():
    tax = env['account.tax'].create({
        'name': f'Isento - {code}',
        'type_tax_use': 'sale',
        'amount': 0.0,
        'l10n_pt_exemption_code': code,
        'l10n_pt_exemption_reason': description
    })
```

### IVA Intracomunitário
```python
# IVA 0% para operações intracomunitárias
intra_eu_vat = {
    'name': 'IVA 0% Intracomunitário',
    'amount': 0.0,
    'l10n_pt_exemption_code': 'M12',
    'type_tax_use': 'sale'
}
```

---

## 📈 Mapas de IVA

### Tipos de Mapas Obrigatórios

#### 1. Declaração Periódica de IVA
**Periodicidade**: Mensal ou Trimestral

#### 2. Listagem Intracomunitária
**Periodicidade**: Mensal (se ultrapassar limites)

#### 3. VIES (VAT Information Exchange System)
**Periodicidade**: Mensal

### Como Configurar

#### 1. Configuração Base
```
Accounting > Reports > Tax Reports:
✅ Enable VAT Reporting
✅ Configure tax report mapping
✅ Set up VIES reporting
```

#### 2. Mapeamento de Impostos
```python
# Configuração automática de relatórios
vat_report_config = {
    'sale_base_23': 'Campo 01 - Vendas Taxa Normal',
    'sale_tax_23': 'Campo 02 - IVA Taxa Normal',
    'purchase_base_23': 'Campo 10 - Compras Taxa Normal',
    'purchase_tax_23': 'Campo 11 - IVA Dedutível'
}
```

### Como Tirar os Mapas

#### Via Interface:
```
1. Accounting > Reporting > Tax Report
2. Selecionar período
3. Escolher formato (PDF/Excel/XML)
4. Gerar relatório
```

#### Via Código:
```python
# Geração automática
def generate_vat_report(date_from, date_to):
    report = env['account.generic.tax.report']
    return report.get_report_values(date_from, date_to)
```

#### Campos Principais do Mapa:
- **Campo 01**: Operações sujeitas à taxa normal
- **Campo 02**: IVA da taxa normal
- **Campo 03**: Operações sujeitas à taxa intermédia  
- **Campo 04**: IVA da taxa intermédia
- **Campo 05**: Operações sujeitas à taxa reduzida
- **Campo 06**: IVA da taxa reduzida
- **Campo 10**: IVA dedutível
- **Campo 11**: IVA apurado

---

## 📋 SAF-T (AT)

### O que é o SAF-T?
**Standard Audit File for Tax** - Arquivo digital normalizado exigido pela AT para auditorias fiscais.

### Como Funciona

#### 1. Estrutura do Ficheiro:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<AuditFile>
    <Header>...</Header>
    <MasterFiles>...</MasterFiles>
    <GeneralLedgerEntries>...</GeneralLedgerEntries>
    <SourceDocuments>...</SourceDocuments>
</AuditFile>
```

#### 2. Periodicidade:
- **Anual**: Obrigatório até 31 de julho
- **A pedido**: Durante inspeções fiscais

### Configuração no Odoo

#### 1. Módulo Base:
```python
# Instalação automática
modules_to_install = [
    'l10n_pt_saft',
    'account_saft',
    'l10n_pt_reports'
]
```

#### 2. Configuração de Empresa:
```
Accounting > Configuration > SAF-T:
- Tax Registration Number: NIF da empresa
- Company Registration Number: Matrícula
- Legal Form: Tipo de sociedade
- Head Office Address: Sede social
```

#### 3. Mapeamento de Contas:
```python
# Configuração automática baseada no SNC
saft_mapping = {
    'account_11': {'grouping_category': 'GA', 'nature': 'D'},
    'account_21': {'grouping_category': 'GR', 'nature': 'D'}, 
    'account_22': {'grouping_category': 'GP', 'nature': 'C'}
}
```

### Como Gerar SAF-T

#### Via Interface:
```
1. Accounting > Reporting > SAF-T
2. Selecionar ano fiscal
3. Escolher tipo (Contabilidade/Faturação)
4. Gerar arquivo XML
5. Validar estrutura
6. Download
```

#### Via Código:
```python
def generate_saft(company, date_from, date_to):
    saft_report = env['l10n_pt.saft.report']
    return saft_report.generate_saft_file(
        company, date_from, date_to
    )
```

### Validação Automática:
- ✅ Estrutura XML conforme XSD da AT
- ✅ Valores de controlo corretos
- ✅ Hash dos documentos
- ✅ Sequências numéricas

### Como Enviar para a AT

#### Portal das Finanças:
```
1. Login no Portal das Finanças
2. Entregar > SAF-T (PT)
3. Upload do arquivo XML
4. Validação automática
5. Submissão
```

#### Integração Automática (futuro):
```python
# API direta com AT (em desenvolvimento)
def submit_saft_to_at(saft_file):
    at_api.submit_saft(
        nif=company.vat,
        file=saft_file,
        year=fiscal_year
    )
```

---

## 🚚 Guias de Transporte e Remessa

### Tipos de Documentos de Transporte

#### 1. Guia de Transporte (GT)
**Quando usar**: Transporte de mercadorias próprias

#### 2. Guia de Remessa (GR)  
**Quando usar**: Remessa para clientes sem faturação imediata

#### 3. Guia de Consignação (GC)
**Quando usar**: Mercadorias em depósito no cliente

### Configuração no Odoo

#### 1. Tipos de Operação:
```
Inventory > Configuration > Operations Types:
- Delivery Orders (Guias de Remessa)
- Internal Transfers (Transferências)
- Receipts (Receções)
```

#### 2. Campos Obrigatórios:
```python
required_fields = [
    'partner_id',           # Destinatário
    'origin_address',       # Morada de origem  
    'destination_address',  # Morada de destino
    'vehicle_plate',        # Matrícula do veículo
    'driver_name',          # Nome do condutor
    'transport_date'        # Data de transporte
]
```

#### 3. Numeração:
```python
# Sequência automática
sequence_config = {
    'name': 'Guias de Transporte',
    'code': 'stock.picking.gt',
    'prefix': 'GT%(year)s',
    'padding': 6,
    'number_increment': 1
}
```

### Integração com InvoiceXpress

#### Geração Automática:
```python
def create_transport_guide(picking):
    if picking.picking_type_code == 'outgoing':
        ix_guide = invoicexpress_api.create_transport_guide({
            'client': picking.partner_id.invoicexpress_id,
            'items': get_picking_items(picking),
            'vehicle_plate': picking.vehicle_plate,
            'driver_name': picking.driver_name
        })
        picking.invoicexpress_guide_id = ix_guide.id
```

### Campos Obrigatórios AT:
- **ATCUD**: Código único do documento
- **Hash**: Assinatura digital
- **QR Code**: Para validação móvel
- **Data e hora**: De emissão e transporte

---

## 📊 Relatórios Contabilísticos

### 1. Balancetes

#### Tipos de Balancetes:

##### A. Balancete Geral
```python
def trial_balance_report(date_from, date_to):
    return {
        'account_code': 'Código da conta',
        'account_name': 'Nome da conta', 
        'debit': 'Movimento a débito',
        'credit': 'Movimento a crédito',
        'balance': 'Saldo final'
    }
```

##### B. Balancete por Períodos
```
Accounting > Reporting > Trial Balance:
- Comparison: Previous Period
- Show hierarchy: Yes
- Show zero balance: No
```

##### C. Balancete Analítico
```python
# Com breakdown por centro de custo
analytic_trial_balance = {
    'account_id': account,
    'analytic_account_id': cost_center,
    'debit': debit_amount,
    'credit': credit_amount
}
```

#### Configuração:
```
1. Accounting > Reporting > Trial Balance
2. Filtros:
   - Date Range: Período desejado
   - Accounts: Todas ou específicas
   - Analytic Accounts: Se aplicável
3. Options:
   - Show Hierarchy: Estrutura de contas
   - Show Zero Balance: Contas sem movimento
```

### 2. Contas Correntes

#### A. Clientes (Aging Report)
```python
def customer_aging_report():
    return {
        'partner_name': 'Nome do cliente',
        'current': 'Valores correntes (0-30 dias)',
        'age_30': 'Vencido 30-60 dias',
        'age_60': 'Vencido 60-90 dias', 
        'age_90': 'Vencido +90 dias',
        'total': 'Total em dívida'
    }
```

#### B. Fornecedores
```
Accounting > Reporting > Aged Payable:
- As of Date: Data de referência
- Target Moves: All Posted Entries
- Account Type: Payable
```

#### C. Extractos de Conta
```python
# Movimentos detalhados por cliente/fornecedor
def partner_ledger(partner_id, date_from, date_to):
    moves = env['account.move.line'].search([
        ('partner_id', '=', partner_id),
        ('date', '>=', date_from),
        ('date', '<=', date_to)
    ])
    return format_partner_statement(moves)
```

### 3. Demonstrações de Resultados

#### A. Demonstração de Resultados Simples
```python
income_statement_structure = {
    'Vendas e Prestações de Serviços': {
        'accounts': ['71*', '72*'],
        'nature': 'credit'
    },
    'Custo das Vendas': {
        'accounts': ['61*'],
        'nature': 'debit'  
    },
    'Fornecimentos e Serviços Externos': {
        'accounts': ['62*'],
        'nature': 'debit'
    },
    'Gastos com Pessoal': {
        'accounts': ['63*'], 
        'nature': 'debit'
    },
    'Resultado Líquido': {
        'calculation': 'rendimentos - gastos'
    }
}
```

#### B. Demonstração de Resultados por Natureza
```
Contabilidade SNC:
├── Vendas e serviços prestados
├── Subsídios à exploração
├── Variação nos inventários  
├── Trabalhos para a própria entidade
├── CMVMC (Custo mercadorias vendidas)
├── Fornecimentos e serviços externos
├── Gastos com pessoal
├── Imparidade de inventários
├── Imparidade de dívidas a receber
├── Provisões
├── Imparidade de investimentos
├── Aumentos/diminuições de justo valor
├── Outros rendimentos e ganhos
├── Outros gastos e perdas
├── Resultado antes de depreciações
├── Gastos/reversões de depreciação
├── Resultado operacional
└── Resultado líquido do período
```

#### C. Configuração no Odoo:
```
Accounting > Reporting > Profit and Loss:
- Comparison: Previous Period/Budget
- Show Hierarchy: Yes
- Show Foreign Currency: If applicable
```

### Como Configurar Cada Relatório

#### 1. Personalização de Relatórios:
```python
# Criação de relatório customizado
custom_report = env['account.financial.html.report'].create({
    'name': 'Relatório Personalizado VK',
    'line_ids': create_report_lines()
})
```

#### 2. Templates de Relatório:
```xml
<!-- Template para relatórios PDF -->
<template id="custom_financial_report">
    <div class="page">
        <div class="header">
            <h2>VK Commodities - Relatório Financeiro</h2>
        </div>
        <div class="content">
            <!-- Conteúdo do relatório -->
        </div>
    </div>
</template>
```

#### 3. Automação de Relatórios:
```python
# Geração automática mensal
def auto_generate_reports():
    for company in env['res.company'].search([]):
        # Balancete mensal
        trial_balance = generate_trial_balance(company)
        # Demonstração de resultados
        income_statement = generate_income_statement(company)
        # Envio por email
        send_reports_by_email(company, [trial_balance, income_statement])
```

---

## 💰 Centros de Custo

### O que são Centros de Custo?

Centros de custo permitem segregar gastos e receitas por departamentos, projetos ou áreas de negócio para análise de rentabilidade.

### Como Funcionam no Odoo

#### 1. Estrutura Hierárquica:
```
VK Commodities
├── Administração
│   ├── Direção Geral
│   ├── Recursos Humanos
│   └── Contabilidade
├── Comercial
│   ├── Vendas Nacionais
│   ├── Vendas Exportação
│   └── Marketing
└── Operações
    ├── Compras
    ├── Armazém
    └── Logística
```

### Implementação

#### 1. Configuração Base:
```
Accounting > Configuration > Analytic Accounting:
✅ Analytic Accounts
✅ Analytic Distribution
✅ Analytic Tags
```

#### 2. Criação de Centros de Custo:
```python
# Via código para automação
cost_centers = [
    {'name': 'Administração', 'code': 'ADM', 'parent_id': False},
    {'name': 'Direção Geral', 'code': 'ADM-DG', 'parent_id': 'ADM'},
    {'name': 'Comercial', 'code': 'COM', 'parent_id': False},
    {'name': 'Vendas', 'code': 'COM-VEN', 'parent_id': 'COM'}
]

for cc in cost_centers:
    env['account.analytic.account'].create(cc)
```

#### 3. Distribuição Automática:
```python
# Regras de distribuição
distribution_rules = {
    'account_621': {  # Rendas
        'ADM': 0.4,   # 40% Administração
        'COM': 0.3,   # 30% Comercial
        'OPE': 0.3    # 30% Operações
    },
    'account_622': {  # Electricidade  
        'ADM': 0.3,
        'OPE': 0.7    # Maior consumo no armazém
    }
}
```

### Relatórios de Centros de Custo

#### 1. Análise de Rentabilidade:
```python
def cost_center_profitability(center_id, date_from, date_to):
    revenues = get_analytic_revenues(center_id, date_from, date_to)
    costs = get_analytic_costs(center_id, date_from, date_to) 
    return {
        'center_name': center.name,
        'revenues': revenues,
        'costs': costs,
        'profit': revenues - costs,
        'margin': (revenues - costs) / revenues * 100
    }
```

#### 2. Comparação Orçamental:
```
Accounting > Reporting > Analytic Reports:
- Budget vs Actual by Analytic Account
- Variance Analysis
- Trend Analysis
```

### Casos de Uso Práticos:

#### A. Controlo de Projetos:
```python
# Centro de custo por projeto
project_cc = env['account.analytic.account'].create({
    'name': f'Projeto Cliente {client.name}',
    'partner_id': client.id,
    'plan_id': project_plan.id
})
```

#### B. Análise Departamental:
```python
# Relatório mensal por departamento
def monthly_department_report():
    departments = env['account.analytic.account'].search([
        ('account_type', '=', 'normal')
    ])
    for dept in departments:
        generate_department_analysis(dept)
```

---

## 📈 Contabilidade Analítica

### Conceitos Base

A contabilidade analítica complementa a contabilidade geral, fornecendo informação detalhada sobre custos, rentabilidade e performance por diferentes dimensões.

### Implementação no Odoo

#### 1. Planos Analíticos:
```python
# Diferentes dimensões de análise
analytic_plans = [
    {
        'name': 'Centros de Custo',
        'code': 'CC',
        'applicability': 'mandatory'
    },
    {
        'name': 'Projetos', 
        'code': 'PROJ',
        'applicability': 'optional'
    },
    {
        'name': 'Produtos',
        'code': 'PROD', 
        'applicability': 'optional'
    }
]
```

#### 2. Distribuição Multi-Dimensional:
```python
# Exemplo: Gasto repartido por múltiplas dimensões
expense_distribution = {
    'account_id': account_625,  # Deslocações
    'amount': 1000.0,
    'analytic_distribution': {
        f'{cc_plan.id}__{admin_cc.id}': 50.0,      # 50% Administração
        f'{cc_plan.id}__{sales_cc.id}': 50.0,      # 50% Comercial
        f'{proj_plan.id}__{project_a.id}': 100.0   # 100% Projeto A
    }
}
```

### Configuração Avançada

#### 1. Regras de Distribuição:
```python
# Distribuição automática baseada em critérios
class AnalyticDistribution(models.Model):
    _name = 'analytic.distribution.rule'
    
    account_id = fields.Many2one('account.account')
    criteria = fields.Selection([
        ('employee', 'Por colaborador'),
        ('product', 'Por produto'),
        ('location', 'Por localização')
    ])
    distribution = fields.Json()
```

#### 2. Integração com Módulos:
```python
# Integração com vendas
def _prepare_invoice_line_analytic(self):
    analytic_distribution = {}
    
    # Centro de custo por vendedor
    if self.salesperson_id:
        cc = self.salesperson_id.analytic_account_id
        analytic_distribution[f'{cc_plan.id}__{cc.id}'] = 100.0
    
    # Projeto se aplicável  
    if self.project_id:
        proj = self.project_id.analytic_account_id
        analytic_distribution[f'{proj_plan.id}__{proj.id}'] = 100.0
        
    return analytic_distribution
```

### Relatórios Analíticos

#### 1. Análise de Margens:
```python
def product_margin_analysis(product_id, date_from, date_to):
    sales = get_product_sales(product_id, date_from, date_to)
    direct_costs = get_product_direct_costs(product_id, date_from, date_to)
    indirect_costs = get_allocated_costs(product_id, date_from, date_to)
    
    return {
        'product': product_id.name,
        'sales': sales,
        'direct_costs': direct_costs,
        'indirect_costs': indirect_costs,
        'gross_margin': sales - direct_costs,
        'net_margin': sales - direct_costs - indirect_costs,
        'margin_percentage': (sales - direct_costs - indirect_costs) / sales * 100
    }
```

#### 2. Dashboard Analítico:
```xml
<!-- Dashboard para gestão -->
<dashboard>
    <view type="graph" name="cost_center_performance"/>
    <view type="pivot" name="profitability_analysis"/>
    <view type="kanban" name="project_overview"/>
</dashboard>
```

### Automações Analíticas

#### 1. Alocação de Custos Indiretos:
```python
# Distribuição mensal automática
@api.model
def monthly_cost_allocation(self):
    # Custos a distribuir (ex: renda, seguros)
    shared_costs = self.env['account.move.line'].search([
        ('account_id.code', 'like', '62%'),
        ('analytic_distribution', '=', False),
        ('date', '>=', month_start),
        ('date', '<=', month_end)
    ])
    
    for cost in shared_costs:
        # Distribuir baseado em critério (ex: % vendas)
        distribution = calculate_distribution(cost)
        cost.analytic_distribution = distribution
```

#### 2. Controlo Orçamental:
```python
def budget_control_alert(self):
    for budget_line in self.budget_line_ids:
        spent = budget_line.practical_amount
        budgeted = budget_line.planned_amount
        
        if spent > budgeted * 0.9:  # 90% do orçamento
            self.send_budget_alert(budget_line)
```

---

## 🔧 Troubleshooting

### Problemas Comuns e Soluções

#### 1. Erro na Instalação de Módulos
```bash
# Limpar cache Python
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

# Restart Odoo server
./scripts/run.sh
```

#### 2. Problemas de Sincronização InvoiceXpress
```python
# Verificar configuração API
def check_invoicexpress_connection():
    try:
        ix_api = InvoiceXpressAPI(api_key, account_name)
        response = ix_api.test_connection()
        return response.status_code == 200
    except Exception as e:
        _logger.error(f"InvoiceXpress connection failed: {e}")
        return False
```

#### 3. SAF-T com Erros de Validação
```python
# Verificação antes da geração
def validate_saft_data(date_from, date_to):
    errors = []
    
    # Verificar sequências de documentos
    invoices = env['account.move'].search([
        ('move_type', 'in', ['out_invoice', 'out_refund']),
        ('date', '>=', date_from),
        ('date', '<=', date_to)
    ])
    
    for invoice in invoices:
        if not invoice.l10n_pt_hash:
            errors.append(f"Fatura {invoice.name} sem hash")
            
    return errors
```

#### 4. Performance de Relatórios
```python
# Otimização de consultas
def optimized_trial_balance(date_from, date_to):
    # Usar raw SQL para performance
    query = """
        SELECT account_id, SUM(debit) as debit, SUM(credit) as credit
        FROM account_move_line aml
        JOIN account_move am ON aml.move_id = am.id
        WHERE am.state = 'posted'
        AND aml.date BETWEEN %s AND %s
        GROUP BY account_id
    """
    env.cr.execute(query, (date_from, date_to))
    return env.cr.dictfetchall()
```

### Logs e Debugging

#### 1. Configuração de Logs:
```python
# odoo.conf
log_level = debug
log_handler = :INFO,werkzeug:CRITICAL,odoo.addons.account:DEBUG
```

#### 2. Debug Specific Issues:
```python
import logging
_logger = logging.getLogger(__name__)

def debug_invoice_creation(self):
    _logger.debug(f"Creating invoice for partner {self.partner_id.name}")
    _logger.debug(f"Invoice lines: {self.invoice_line_ids}")
```

---

## 📞 Suporte e Contactos

### Equipa de Desenvolvimento VK
- **Email**: suporte@vkcommodities.pt
- **Telefone**: +351 XXX XXX XXX
- **Horário**: 09:00 - 18:00 (Portugal)

### Recursos Úteis
- [Documentação Oficial Odoo](https://www.odoo.com/documentation/18.0/)
- [Autoridade Tributária](https://www.portaldasfinancas.gov.pt/)
- [InvoiceXpress API](https://invoicexpress.com/api)

---

## 📝 Changelog

### Versão 18.0.1.0.0 (2024-08-14)
- ✅ Configuração inicial módulos contabilidade
- ✅ Integração InvoiceXpress
- ✅ Plano de contas SNC
- ✅ Configuração SAF-T
- ✅ Relatórios contabilísticos base

### Próximas Funcionalidades
- 🔄 API direta com AT
- 🔄 Relatórios avançados BI
- 🔄 Dashboards executivos
- 🔄 Integração bancária automática

---

*Este documento é mantido atualizado pela equipa de desenvolvimento VK Commodities. Última atualização: 14 de agosto de 2024.*
