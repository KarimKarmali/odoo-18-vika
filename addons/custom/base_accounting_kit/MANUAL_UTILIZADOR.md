# Manual do Utilizador - Contabilidade VK Commodities
## Sistema de Gestão Financeira Odoo 18

![Versão](https://img.shields.io/badge/version-18.0.1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-Manual--Utilizador-green.svg)

---

## 📋 Índice

1. [Introdução](#introdução)
2. [Acesso e Navegação](#acesso-e-navegação)
3. [Módulo Vendas](#módulo-vendas)
4. [Módulo Compras](#módulo-compras)
5. [Módulo Inventário](#módulo-inventário)
6. [Módulo Faturação](#módulo-faturação)
7. [Módulo Contabilidade](#módulo-contabilidade)
8. [Configuração de Artigos](#configuração-de-artigos)
9. [Correção de Lançamentos](#correção-de-lançamentos)
10. [InvoiceXpress](#invoicexpress)
11. [IVA e Impostos](#iva-e-impostos)
12. [Mapas de IVA](#mapas-de-iva)
13. [SAF-T para AT](#saf-t-para-at)
14. [Guias de Transporte](#guias-de-transporte)
15. [Relatórios Financeiros](#relatórios-financeiros)
16. [Centros de Custo](#centros-de-custo)
17. [Perguntas Frequentes](#perguntas-frequentes)

---

## 🎯 Introdução

Este manual destina-se aos **utilizadores finais** do sistema Odoo da VK Commodities. Aqui encontrará instruções passo-a-passo para usar todas as funcionalidades contabilísticas e fiscais.

### O que vai aprender:
- ✅ Como navegar no sistema
- ✅ Como criar e gerir documentos
- ✅ Como configurar artigos para contabilidade
- ✅ Como corrigir lançamentos contabilísticos
- ✅ Como gerar o SAF-T para a AT
- ✅ Como tirar relatórios e mapas

---

## 🔐 Acesso e Navegação

### Como Fazer Login
1. **Abrir o navegador** e ir para: `http://localhost:8069`
2. **Introduzir credenciais**:
   - **Database**: `vk_dev` (ou nome da base de dados)
   - **Email**: seu.email@vkcommodities.pt
   - **Password**: sua palavra-passe

### Interface Principal
```
┌─────────────────────────────────────────────┐
│ [🏠] VK Commodities    [👤] Seu Nome  [⚙️]   │
├─────────────────────────────────────────────┤
│ 📊 Dashboard  💰 Accounting  🛒 Sales       │
│ 📦 Inventory  🔄 Purchase   📋 Invoicing    │
├─────────────────────────────────────────────┤
│           Conteúdo Principal                │
│                                             │
└─────────────────────────────────────────────┘
```

### Menu Principal
- **Dashboard**: Visão geral da empresa
- **Accounting**: Contabilidade e finanças
- **Sales**: Vendas e clientes
- **Purchase**: Compras e fornecedores
- **Inventory**: Stock e armazém
- **Invoicing**: Faturação

---

## 🛒 Módulo Vendas

### Como Criar um Orçamento

#### Passo 1: Aceder ao Menu
```
Sales > Orders > Quotations
```

#### Passo 2: Criar Novo Orçamento
1. Clicar em **[Create]**
2. **Preencher campos obrigatórios**:
   - **Customer**: Selecionar cliente (obrigatório)
   - **Expiration**: Data de validade
   - **Salesperson**: Comercial responsável

#### Passo 3: Adicionar Produtos
1. Clicar em **Add a line**
2. **Selecionar produto** na lista
3. **Quantidade**: Introduzir quantidade
4. **Preço**: Confirmar/alterar preço unitário
5. **Impostos**: Verificar se IVA está correto

#### Passo 4: Finalizar Orçamento
1. **Save**: Guardar o orçamento
2. **Send by Email**: Enviar ao cliente (opcional)
3. **Confirm Sale**: Converter em encomenda

### Como Converter Orçamento em Venda
```
Quotations > [Selecionar orçamento] > Confirm Sale
```
**Resultado**: Cria automaticamente uma Sales Order

---

## 🔄 Módulo Compras

### Como Criar Pedido de Cotação (RFQ)

#### Passo 1: Menu de Compras
```
Purchase > Orders > Requests for Quotation
```

#### Passo 2: Novo RFQ
1. **Create**: Novo pedido
2. **Vendor**: Selecionar fornecedor
3. **Order Date**: Data da encomenda
4. **Expected Arrival**: Data prevista de entrega

#### Passo 3: Linhas de Produtos
1. **Add a line**: Adicionar produto
2. **Product**: Selecionar da lista
3. **Quantity**: Quantidade necessária
4. **Unit Price**: Preço unitário
5. **Taxes**: Verificar IVA de compra

#### Passo 4: Confirmação
1. **Save**: Guardar RFQ
2. **Send by Email**: Enviar ao fornecedor
3. **Confirm Order**: Confirmar encomenda

---

## 🔧 Configuração de Artigos

### Configuração Contabilística de Produtos

Esta secção explica como configurar produtos para que sejam automaticamente lançados nas contas contabilísticas corretas.

#### Acesso à Configuração
```
Inventory > Products > Products > [Selecionar Produto] > Edit
Separador: "Accounting"
```

### Campos Importantes

#### 1. Expense Account (Conta de Gasto)
**Para que serve**: Conta usada quando **compra** este produto

**Como configurar**:
```
Accounting Tab > Expense Account
```

**Exemplos de contas**:
- **Mercadorias**: `32 - Mercadorias`
- **Matérias-primas**: `33 - Matérias-primas, subsidiárias e de consumo`
- **Serviços**: `622 - Fornecimentos e serviços externos`
- **Combustíveis**: `6224 - Combustíveis`
- **Material escritório**: `6226 - Material de escritório`

#### 2. Income Account (Conta de Rendimento)
**Para que serve**: Conta usada quando **vende** este produto

**Como configurar**:
```
Accounting Tab > Income Account
```

**Exemplos de contas**:
- **Vendas nacionais**: `711 - Vendas`
- **Vendas exportação**: `712 - Prestações de serviços`
- **Serviços**: `72 - Prestações de serviços`

#### 3. Customer Taxes (IVA de Venda)
**Como configurar**:
```
Accounting Tab > Customer Taxes
```

**Opções disponíveis**:
- **IVA 23%**: Taxa normal
- **IVA 13%**: Taxa intermédia
- **IVA 6%**: Taxa reduzida
- **Isento M01**: Artigo 16º CIVA
- **Isento M04**: Regime especial
- **IVA 0% Intracomunitário**: Vendas UE

#### 4. Vendor Taxes (IVA de Compra)
**Como configurar**:
```
Accounting Tab > Vendor Taxes
```

**Configuração típica**: Mesmo IVA da venda

### Configuração por Categoria

#### Método Alternativo: Por Categoria de Produto
```
Inventory > Configuration > Product Categories
[Selecionar categoria] > Separador "Accounting"
```

**Vantagem**: Todos os produtos da categoria herdam automaticamente as configurações.

### Exemplos Práticos

#### Exemplo 1: Produto "Café"
```
┌─────────────────────────────────────────┐
│ Nome: Café Premium                      │
│ Categoria: Mercadorias > Alimentares    │
│                                         │
│ ACCOUNTING:                             │
│ ├─ Expense Account: 32 - Mercadorias    │
│ ├─ Income Account: 711 - Vendas         │
│ ├─ Customer Taxes: IVA 13%              │
│ └─ Vendor Taxes: IVA 13%                │
└─────────────────────────────────────────┘
```

#### Exemplo 2: Serviço "Consultoria"
```
┌─────────────────────────────────────────┐
│ Nome: Consultoria Gestão                │
│ Categoria: Serviços                     │
│                                         │
│ ACCOUNTING:                             │
│ ├─ Expense Account: 622 - FSE           │
│ ├─ Income Account: 72 - Serviços        │
│ ├─ Customer Taxes: IVA 23%              │
│ └─ Vendor Taxes: IVA 23%                │
└─────────────────────────────────────────┘
```

### Verificação da Configuração

#### Como Testar se Está Correto
1. **Criar fatura de teste** com o produto
2. **Verificar**: Conta contabilística usada
3. **Ir para**: `Accounting > Accounting > Journal Entries`
4. **Procurar**: Movimento da fatura
5. **Confirmar**: Conta está correta

#### Exemplo de Movimento Correto:
```
Data: 14/08/2024
Referência: INV/2024/0001

Linhas:
├─ Conta 21100 (Clientes) ........ 123,00 € (Débito)
├─ Conta 711 (Vendas) ............ 100,00 € (Crédito)
└─ Conta 2331 (IVA Liquidado) ..... 23,00 € (Crédito)
```

---

## ✏️ Correção de Lançamentos

### Quando Corrigir Lançamentos

#### Situações Comuns:
- ❌ **Conta errada**: Produto lançado na conta incorreta
- ❌ **Valor errado**: Erro no montante
- ❌ **Data errada**: Data de movimento incorreta
- ❌ **IVA errado**: Taxa de IVA incorreta
- ❌ **Cliente/Fornecedor errado**: Partner incorreto

### Métodos de Correção

#### Método 1: Notas de Crédito (Recomendado)

##### Para Faturas de Venda:
```
Invoicing > Customers > Invoices
[Selecionar fatura errada] > Add Credit Note
```

**Passo a passo**:
1. **Add Credit Note**: Criar nota de crédito
2. **Reason**: Motivo da correção
3. **Lines**: Verificar linhas a corrigir
4. **Confirm**: Confirmar nota de crédito
5. **Create**: Nova fatura correta

##### Para Faturas de Compra:
```
Purchase > Vendor Bills
[Selecionar fatura] > Add Credit Note
```

#### Método 2: Lançamento de Correção

##### Quando Usar:
- Erros em lançamentos manuais
- Correções de final de mês
- Ajustes contabilísticos

##### Como Fazer:
```
Accounting > Accounting > Journal Entries > Create
```

**Exemplo de correção**:
```
MOVIMENTO ERRADO:
├─ Conta 622 (FSE) ............... 100,00 € (Débito)
└─ Conta 22100 (Fornecedores) .... 100,00 € (Crédito)

LANÇAMENTO DE CORREÇÃO:
├─ Conta 622 (FSE) ............... 100,00 € (Crédito)
├─ Conta 631 (Gastos Pessoal) .... 100,00 € (Débito)
└─ Referência: "Correção movimento XX"
```

### Correções Específicas

#### 1. Corrigir Conta Contabilística

##### Situação: Produto lançado na conta errada

**Solução A - Via Produto**:
```
1. Inventory > Products > [Produto] > Edit
2. Accounting Tab > Alterar conta
3. Nota: Só afeta movimentos futuros
```

**Solução B - Lançamento Manual**:
```
Accounting > Journal Entries > Create

Linhas:
├─ Conta Errada .................. 100,00 € (Crédito)
├─ Conta Correta ................ 100,00 € (Débito)
└─ Referência: "Correção conta produto X"
```

#### 2. Corrigir Valor de IVA

##### Situação: Taxa de IVA incorreta na fatura

**Solução**:
```
1. Nota de crédito da fatura completa
2. Nova fatura com IVA correto
3. Verificar mapa de IVA do período
```

#### 3. Corrigir Data de Movimento

##### Limitações:
- ⚠️ **Atenção**: Só é possível antes do fecho do período
- ⚠️ **SAF-T**: Pode afetar declarações já enviadas

**Como fazer**:
```
Accounting > Journal Entries
[Selecionar movimento] > Edit > Alterar data
```

### Verificações Após Correção

#### 1. Balancete de Verificação
```
Accounting > Reporting > Trial Balance
Comparar: Antes vs. Depois da correção
```

#### 2. Extracto de Conta
```
Accounting > Reporting > Partner Ledger
Verificar: Movimento do cliente/fornecedor
```

#### 3. Mapas de IVA
```
Accounting > Reporting > Tax Report
Confirmar: IVA está correto
```

### Boas Práticas

#### ✅ Antes de Corrigir:
1. **Backup**: Exportar dados antes de grandes correções
2. **Documentar**: Anotar motivo da correção
3. **Autorização**: Confirmar com responsável

#### ✅ Durante a Correção:
1. **Testar**: Fazer teste em ambiente desenvolvimento
2. **Verificar**: Conferir todos os cálculos
3. **Validar**: Confirmar balanceamento

#### ✅ Após Correção:
1. **Relatórios**: Gerar relatórios de verificação
2. **Comunicar**: Informar equipa sobre alterações
3. **Arquivo**: Guardar documentação da correção

---

## 📋 SAF-T para AT

### O que é o SAF-T?

O **SAF-T (PT)** é o arquivo digital normalizado exigido pela Autoridade Tributária para auditorias fiscais. Contém todos os dados contabilísticos e fiscais da empresa.

### Quando é Obrigatório

#### Entrega MENSAL:
- **Prazo**: Até dia 5 do mês seguinte
- **Período**: Mês anterior completo  
- **Exemplo**: SAF-T de agosto 2024 entregue até 5 de setembro 2024
- **Penalizações**: Multas por atraso na entrega

#### Inspeções Fiscais:
- **A pedido**: Durante auditorias da AT
- **Prazo**: Normalmente 5 dias úteis

### Como Gerar SAF-T no Odoo

#### Passo 1: Aceder ao Menu
```
Accounting > Reporting > SAF-T Export
```

#### Passo 2: Configurar Parâmetros
**Campos obrigatórios**:
- **Company**: Empresa (VK Commodities)
- **Start Date**: 01/08/2024 (início do mês)
- **End Date**: 31/08/2024 (fim do mês)
- **Type**: Accounting (contabilidade)

#### Passo 3: Opções Avançadas
```
Advanced Options:
```
- **Export Type**: Complete (completo)
- **Include Zero Balance**: No (recomendado)
- **Audit File Version**: 1.04_01 (mais recente)

#### Passo 4: Gerar Arquivo
```
Generate SAF-T > Create Export
```
**Tempo**: 5-30 minutos dependendo do volume

#### Passo 5: Download
```
State: Ready > Download XML File
```

### Como Obter o Ficheiro XML para Enviar à AT

#### **PASSO A PASSO DETALHADO:**

##### 1. Localização do Ficheiro no Odoo:
```
Accounting > Reporting > SAF-T (PT)
```

##### 2. Ver Lista de Exports Criados:
- Na página SAF-T, vai ver uma lista de todos os exports já gerados
- Cada linha mostra:
  - **Date**: Data de criação
  - **Period**: Período (ex: 01/01/2024 - 31/12/2024)
  - **State**: Estado (Draft/Running/Ready/Error)
  - **Actions**: Botões disponíveis

##### 3. Download do Ficheiro XML:
```
[Selecionar linha com State: "Ready"] > Download XML File
```

##### 4. Verificar o Ficheiro Descarregado:
- **Nome do ficheiro**: `SAFT_PT_123456789_2024.xml`
- **Localização**: Pasta Downloads do computador
- **Tamanho**: Deve ter vários MB (não pode estar vazio)

##### 5. Validar o Ficheiro (Opcional mas Recomendado):
```
No Odoo: Export Details > Validation Log
Deve mostrar: "✅ Validation successful"
```

### Como Enviar o XML para a AT

#### Passo 1: Portal das Finanças
1. **Aceder**: [Portal das Finanças](https://www.portaldasfinancas.gov.pt)
2. **Login**: Credenciais da empresa (NIF + palavra-passe)
3. **Menu**: Entregar > Informação Empresarial

#### Passo 2: Submeter SAF-T
```
Portal das Finanças:
Entregar > Informação Empresarial > SAF-T (PT)
```

#### Passo 3: Upload do Ficheiro
1. **Browse**: Selecionar ficheiro XML descarregado
2. **Ano**: Confirmar ano fiscal (2024)
3. **Validate**: Sistema valida estrutura automaticamente
4. **Submit**: Submeter ficheiro

#### Passo 4: Confirmação
- **Recibo**: Guardar comprovativo de entrega
- **Número**: Protocolo de submissão
- **Data**: Data e hora de entrega

### Verificações Importantes Antes de Gerar

#### 1. Fecho Contabilístico:
```
Accounting > Accounting > Lock Dates
Confirmar que todos os meses estão fechados
```

#### 2. Reconciliações Bancárias:
```
Accounting > Bank and Cash > Bank Statements
Todas as reconciliações devem estar completas
```

#### 3. Sequências de Documentos:
```
Invoicing > Configuration > Journals
Verificar que não há falhas na numeração
```

#### 4. Dados da Empresa:
```
Settings > Companies > VK Commodities
Verificar:
- VAT Number: NIF completo (PT123456789)
- Address: Morada completa
- Legal Form: Tipo de sociedade
```

### Resolução de Problemas Comuns

#### Erro: "Dados incompletos"
**Solução**:
1. Verificar configuração da empresa (NIF, morada, etc.)
2. Verificar se todas as contas têm código
3. Confirmar hierarquia do plano de contas

#### Erro: "Sequências quebradas"
**Solução**:
1. Verificar numeração de faturas sem falhas
2. Marcar documentos cancelados como "Cancelled"
3. Confirmar sequências de todos os diários

#### Ficheiro muito grande (>200MB)
**Solução**:
```
Advanced Options:
- Split by Period: Monthly
- Compress: Yes (ZIP)
```

### Arquivo e Retenção

#### Guardar Cópias:
1. **Servidor Odoo**: Backup automático
2. **Computador local**: Pasta específica SAF-T
3. **Cloud/Servidor empresa**: Backup seguro

#### Período de Retenção:
- **Mínimo legal**: 10 anos
- **Formatos**: XML original + PDF de confirmação AT

---

## 📈 Mapas de IVA

### Acesso aos Mapas

#### Menu Principal:
```
Accounting > Reporting > Tax Report
```

### Como Gerar Mapa de IVA

#### Passo 1: Configurar Período
```
Tax Report > Filtros:
```
- **From**: Data início (ex: 01/08/2024)
- **To**: Data fim (ex: 31/08/2024)
- **Tax Units**: Todas as empresas

#### Passo 2: Gerar Relatório
```
Apply > Generate Report
```

#### Passo 3: Exportar
```
Print > Download PDF
ou
Print > Download Excel
```

### Estrutura do Mapa

#### Campos Principais:

**Operações Sujeitas a IVA**:
- **Campo 01**: Base tributável taxa normal (23%)
- **Campo 02**: IVA liquidado taxa normal
- **Campo 03**: Base tributável taxa intermédia (13%)
- **Campo 04**: IVA liquidado taxa intermédia
- **Campo 05**: Base tributável taxa reduzida (6%)
- **Campo 06**: IVA liquidado taxa reduzida

**IVA Dedutível**:
- **Campo 10**: IVA suportado dedutível
- **Campo 11**: IVA dedutível - bens de investimento

**Apuramento**:
- **Campo 20**: IVA liquidado (total campos 02+04+06)
- **Campo 21**: IVA dedutível (total campo 10+11)
- **Campo 22**: IVA a pagar/receber (campo 20 - campo 21)

### Verificações Importantes

#### Antes de Submeter:
1. **Conferir totais**: Comparar com contabilidade
2. **Verificar isenções**: Códigos M01, M04, etc.
3. **Validar datas**: Período correto
4. **Confirmar NIF**: Clientes intracomunitários

#### Relatórios de Apoio:
```
Accounting > Reporting > Sales Report (IVA)
Accounting > Reporting > Purchase Report (IVA)
```

---

## 📊 Relatórios Financeiros

### Menu de Relatórios

#### Acesso Principal:
```
Accounting > Reporting
```

#### Relatórios Disponíveis:
- **Trial Balance**: Balancete
- **Profit and Loss**: Demonstração resultados
- **Balance Sheet**: Balanço
- **Aged Receivable**: Clientes em dívida
- **Aged Payable**: Dívidas a fornecedores

### 1. Balancete (Trial Balance)

#### Como Gerar:
```
Accounting > Reporting > Trial Balance
```

#### Configurações:
**Período**:
- **From**: Data início (ex: 01/08/2024)
- **To**: Data fim (ex: 31/08/2024)

**Opções**:
- **Comparison**: Comparar com período anterior
- **Show Hierarchy**: Ver estrutura de contas
- **Show Zero Balance**: Incluir contas sem movimento

#### Interpretar Resultados:
```
Estrutura do Balancete:
├── Código da Conta
├── Nome da Conta  
├── Débito (movimentos a débito)
├── Crédito (movimentos a crédito)
└── Saldo Final (débito - crédito)
```

### 2. Demonstração de Resultados

#### Como Gerar:
```
Accounting > Reporting > Profit and Loss
```

#### Estrutura Padrão:
```
DEMONSTRAÇÃO DE RESULTADOS:

RENDIMENTOS:
├── Vendas (71) ..................... 100.000 €
├── Prestações Serviços (72) ......... 20.000 €
└── Total Rendimentos ............... 120.000 €

GASTOS:
├── CMVMC (61) ....................... 60.000 €
├── FSE (62) ......................... 30.000 €
├── Gastos Pessoal (63) .............. 20.000 €
└── Total Gastos .................... 110.000 €

RESULTADO LÍQUIDO .................... 10.000 €
```

### 3. Extractos de Conta (Partner Ledger)

#### Para Clientes:
```
Accounting > Reporting > Partner Ledger
Filter: Customer Accounts
```

#### Para Fornecedores:
```
Accounting > Reporting > Partner Ledger  
Filter: Vendor Accounts
```

### Exportação de Relatórios

#### Formatos Disponíveis:
- **PDF**: Para impressão/arquivo
- **Excel**: Para análise adicional
- **CSV**: Para importação noutros sistemas

#### Como Exportar:
```
[Qualquer relatório] > Print > Download PDF/Excel
```

---

## 💰 Centros de Custo

### O que são Centros de Custo?

Os **centros de custo** permitem analisar gastos e receitas por departamento, projeto ou área de negócio, facilitando o controlo de gestão e análise de rentabilidade.

### Configuração Inicial

#### Ativar Contabilidade Analítica:
```
Accounting > Configuration > Settings
Analytic Accounting: ☑️ Enabled
```

#### Criar Centros de Custo:
```
Accounting > Configuration > Analytic Accounts > Create
```

### Estrutura Recomendada VK Commodities

#### Hierarquia por Departamento:
```
VK COMMODITIES
├── 001 - ADMINISTRAÇÃO
│   ├── 001.1 - Direção Geral
│   ├── 001.2 - Recursos Humanos  
│   └── 001.3 - Contabilidade
├── 002 - COMERCIAL
│   ├── 002.1 - Vendas Nacionais
│   ├── 002.2 - Vendas Exportação
│   └── 002.3 - Marketing
└── 003 - OPERAÇÕES
    ├── 003.1 - Compras
    ├── 003.2 - Armazém
    └── 003.3 - Logística
```

### Como Imputar Gastos

#### Método 1: Manual (Lançamentos)
```
Accounting > Journal Entries > Create
```

**Em cada linha**:
- **Account**: Conta contabilística
- **Analytic Account**: Selecionar centro de custo
- **Amount**: Valor a imputar

#### Método 2: Automático (Faturas)
```
Invoicing > Vendor Bills > [Fatura fornecedor]
```

**Em cada linha de fatura**:
- **Product**: Produto/serviço
- **Analytic Distribution**: Distribuir por centros

---

## ❓ Perguntas Frequentes

### Gestão Diária

#### ❓ **Como saber se uma fatura foi enviada para o InvoiceXpress?**
**Resposta**: 
```
Fatura > Tab "InvoiceXpress" > Status: "Sent"
```
Se status = "Draft", clicar em "Send to InvoiceXpress"

#### ❓ **Como corrigir NIF de cliente após faturar?**
**Resposta**:
1. Nota de crédito da fatura original
2. Corrigir NIF do cliente
3. Nova fatura com NIF correto

#### ❓ **Fatura fica sempre em "Draft" - porquê?**
**Resposta**: Verificar se:
- Cliente tem NIF válido
- Produto tem conta contabilística configurada
- IVA está selecionado
- Todos os campos obrigatórios preenchidos

### Contabilidade

#### ❓ **Como saber que contas usar para cada tipo de gasto?**
**Resposta**:
```
Plano de Contas SNC:
- 61: Custo mercadorias vendidas  
- 622: Fornecimentos serviços externos
- 631: Gastos com pessoal
- 64: Depreciações
```

#### ❓ **Balancete não fecha (débitos ≠ créditos) - o que fazer?**
**Resposta**:
1. Verificar lançamentos não confirmados
2. Verificar se há movimentos em rascunho
3. Executar: `Accounting > Actions > Check Integrity`

#### ❓ **Como ver quanto deve um cliente?**
**Resposta**:
```
Accounting > Reporting > Aged Receivable
ou
Customers > [Cliente] > Tab "Accounting"
```

### SAF-T e Fiscalidade

#### ❓ **SAF-T dá erro "sequência quebrada" - como resolver?**
**Resposta**:
Verificar se há documentos cancelados sem estar marcados como tal:
```
Invoicing > All Documents > Filter: "Cancelled"
Verificar numeração sequencial
```

#### ❓ **Onde encontro o ficheiro XML do SAF-T após gerar?**
**Resposta**:
```
Accounting > Reporting > SAF-T (PT)
Lista de exports > [Selecionar] > Download XML File
Ficheiro fica em Downloads: SAFT_PT_[NIF]_[ANO].xml
```

#### ❓ **Mapa de IVA com valores estranhos - porquê?**
**Resposta**:
- Verificar se todas as faturas têm IVA correto
- Confirmar período do relatório
- Verificar faturas de fornecedores com IVA

---

## 📞 Contactos e Suporte

### Equipa VK Commodities

#### Suporte Técnico:
- **Email**: suporte@vkcommodities.pt
- **Telefone**: +351 XXX XXX XXX
- **Horário**: 09:00 - 18:00 (segunda a sexta)

#### Suporte Contabilístico:
- **Email**: contabilidade@vkcommodities.pt
- **Responsável**: [Nome do Responsável]
- **Horário**: 09:00 - 17:00

---

*Este manual é atualizado regularmente pela equipa VK Commodities. Para sugestões de melhoria, contacte suporte@vkcommodities.pt*

**Última atualização**: 14 de agosto de 2024
