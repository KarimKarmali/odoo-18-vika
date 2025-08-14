# 📚 Manual de Contabilidade VIKA - Odoo 18

## 📋 Visão Geral do Sistema

O sistema contábil VIKA integra os **melhores módulos da OCA (Odoo Community Association)** para fornecer uma solução completa de contabilidade e relatórios financeiros. Este manual documenta todos os módulos instalados e como utilizá-los eficientemente.

## ⚖️ IMPORTANTE: Conformidade Legal - Legislação Portuguesa

> **🚨 ATENÇÃO**: Segundo a legislação portuguesa, **faturas confirmadas/emitidas NÃO podem ser alteradas ou anuladas diretamente**.

### 📋 Obrigações Legais

- **Faturas Confirmadas**: Após emissão, ficam inalteráveis
- **Correções**: Apenas através de **Notas de Crédito** ou **Notas de Débito**
- **Integridade**: Documentos fiscais devem manter integridade total
- **Auditoria**: Rastro completo de todas as alterações

### ⚡ Comportamento por Sistema

| Sistema | Permite Alterar Faturas | Conformidade Legal | Solução |
|---------|-------------------------|-------------------|---------|
| **Odoo Padrão** | ❌ SIM (PROBLEMÁTICO) | ❌ NÃO CONFORME | Usar módulos PT + InvoiceXpress |
| **Odoo + InvoiceXpress** | ✅ NÃO (Bloqueado) | ✅ TOTALMENTE CONFORME | Sistema já configurado ✅ |

### 🏆 Módulos Portugueses Instalados

O sistema VIKA tem os seguintes módulos de conformidade:

- `l10n_pt` - Localização base para Portugal
- `l10n_pt_account_invoicexpress` - **Integração com InvoiceXpress**
- `l10n_pt_stock_invoicexpress` - Integração stock com InvoiceXpress
- `l10n_pt_vat` - IVA português

### ✅ Como Trabalhar em Conformidade

1. **Criar Faturas**: Use sempre a integração Odoo → InvoiceXpress
2. **Validar Faturas**: Confirme no InvoiceXpress (fica bloqueada automaticamente)
3. **Correções**:
   - Para erros: Criar **Nota de Crédito**
   - Para valores adicionais: Criar **Nota de Débito**
   - Se necessário: Emitir nova fatura correta
4. **Comunicação AT**: InvoiceXpress comunica automaticamente à Autoridade Tributária

> 💡 **RECOMENDAÇÃO VIKA**: Use sempre o InvoiceXpress para faturas legais. O Odoo serve para gestão interna, relatórios e análises, enquanto o InvoiceXpress garante a conformidade fiscal.

### 🔧 Configuração da Integração

Para configurar a integração InvoiceXpress:

1. Vá a **Contabilidade → Configuração → InvoiceXpress**
2. Introduza as **credenciais API** do InvoiceXpress
3. Configure os **templates de documentos**
4. Teste a **sincronização**
5. Ative a **comunicação automática à AT**

---

### 🎯 Módulos Principais Instalados

| Módulo | Função | Estado |
|--------|--------|--------|
| **account_usability** | Menus em falta + Contabilidade Saxónica | ✅ Ativo |
| **mis_builder** | Construtor de Relatórios MIS | ✅ Ativo |
| **mis_builder_budget** | Orçamentos MIS | ✅ Ativo |
| **account_financial_report** | Relatórios Financeiros Avançados | ✅ Ativo |
| **l10n_pt_account_invoicexpress** | Integração InvoiceXpress | ✅ Ativo |
| **account_asset_management** | Gestão de Ativos Fixos | ✅ Ativo |
| **account_tax_balance** | Balancete Fiscal | ✅ Ativo |
| **partner_statement** | Extratos de Parceiros | ✅ Ativo |

---

## 🎯 Account Usability - Menus em Falta

### Descrição
O módulo **account_usability** resolve um problema comum no Odoo Community: a ausência do menu principal "Contabilidade". Este módulo adiciona todos os menus que normalmente só existem na versão Enterprise.

### Funcionalidades Adicionadas
- ✅ **Menu principal "Contabilidade"** visível
- ✅ **Submenus organizados** por categoria
- ✅ **Contabilidade Saxónica** (opcional)
- ✅ **Tags e Grupos de Contas** acessíveis
- ✅ **Configurações técnicas** expostas

### Como Usar
1. Acesse **Contabilidade** no menu principal
2. Navegue pelos submenus organizados:
   - **Faturas** → Faturas de cliente/fornecedor
   - **Configuração** → Plano de contas, impostos
   - **Relatórios** → Todos os relatórios disponíveis

---

## 📊 MIS Builder - Construtor de Relatórios

### Descrição
O **MIS Builder** é uma ferramenta poderosa para criar **Management Information Systems** - dashboards personalizados com KPIs em linhas e períodos em colunas.

### Conceitos Fundamentais

#### 1. **MIS Reports** - Relatórios Base
- **Definição**: Template do relatório com estrutura e regras
- **Componentes**: 
  - **Linhas**: KPIs e métricas (Receitas, Custos, Margens)
  - **Colunas**: Períodos temporais (Mensal, Trimestral, Anual)
  - **Expressões**: Fórmulas para calcular valores

#### 2. **MIS Report Instances** - Instâncias de Relatórios
- **Definição**: Relatório executado com dados específicos
- **Parâmetros**:
  - **Períodos**: Define datas de início/fim
  - **Empresa**: Multi-empresa suportada
  - **Moeda**: Conversão automática

### Criando um Relatório MIS

#### Passo 1: Criar MIS Report
```
Contabilidade → MIS Reporting → MIS Reports → Criar
```

**Configuração Básica:**
- **Nome**: "Demonstração de Resultados VIKA"
- **Descrição**: "P&L mensal com comparativo"

#### Passo 2: Definir Linhas (KPIs)
```python
# Exemplo de linhas comuns:
Receitas Operacionais    | account_balances
Custos Mercadorias      | -account_balances  
Margem Bruta           | balances[Receitas] - balances[Custos]
Despesas Operacionais   | account_balances
EBITDA                 | balances[Margem] - balances[Despesas]
```

#### Passo 3: Configurar Colunas
- **Tipo**: Período relativo
- **Modo**: Mês atual, mês anterior, YTD
- **Offset**: 0, -1, -2 para comparativos

### Exemplos Práticos

#### 1. **Balanço Patrimonial**
```
Ativo Circulante
├── Caixa e Bancos        → sum(account_balances('111%'))
├── Contas a Receber      → sum(account_balances('121%'))
└── Estoque               → sum(account_balances('131%'))

Passivo Circulante
├── Fornecedores          → sum(account_balances('211%'))
├── Impostos a Pagar      → sum(account_balances('221%'))
└── Empréstimos           → sum(account_balances('231%'))
```

#### 2. **Fluxo de Caixa**
```
Entrada Operacional
├── Recebimentos Clientes → moves('1110%', period)
├── Outros Recebimentos   → moves('1190%', period)

Saída Operacional  
├── Pagto Fornecedores    → moves('2110%', period)
├── Pagto Funcionários    → moves('2120%', period)
```

### MIS Builder Budget - Orçamentos

#### Funcionalidades
- **Orçamentos por Conta**: Budget detalhado por conta contábil
- **Orçamentos por Item**: Budget por centro de custo/projeto
- **Comparativo Real vs Budget**: Análise de desvios
- **Projeções**: Extrapolação de tendências

#### Criando um Orçamento
1. **Contabilidade → MIS Reporting → MIS Budgets**
2. **Definir períodos** (mensal/trimestral)
3. **Inserir valores** por conta ou item
4. **Vincular ao MIS Report** para comparativos

---

## 📈 Account Financial Report - Relatórios Avançados

### Relatórios Disponíveis

#### 1. **General Ledger** - Razão Geral
- **Função**: Movimentos detalhados por conta
- **Filtros**: Data, conta, parceiro, diário
- **Exportação**: PDF, Excel, QWeb

#### 2. **Trial Balance** - Balancete de Verificação
- **Função**: Saldos de todas as contas
- **Níveis**: Conta analítica, parceiro
- **Comparativo**: Período anterior, orçamento

#### 3. **Aged Partner Balance** - Aging de Parceiros
- **Função**: Análise de vencimentos (30/60/90 dias)
- **Tipos**: Contas a receber, contas a pagar
- **Alertas**: Clientes em atraso, limite crédito

#### 4. **Open Items** - Itens em Aberto
- **Função**: Faturas não reconciliadas
- **Agrupamento**: Por parceiro, data vencimento
- **Ações**: Reconciliação em lote

### Como Gerar Relatórios
1. **Contabilidade → Relatórios → [Escolher Relatório]**
2. **Configurar filtros**:
   - **Data**: De/Até ou período fiscal
   - **Contas**: Específicas ou todas
   - **Parceiros**: Filtro por cliente/fornecedor
3. **Gerar**: PDF para impressão, Excel para análise

---

## 🇵🇹 InvoiceXpress - Integração Portugal

### Descrição
A integração **InvoiceXpress** permite sincronização automática entre Odoo e a plataforma InvoiceXpress, cumprindo as obrigações fiscais portuguesas.

### Módulos da Integração

#### 1. **l10n_pt_account_invoicexpress**
- **Sincronização de faturas** Odoo → InvoiceXpress
- **Compliance** com AT (Autoridade Tributária)
- **Numeração sequencial** obrigatória
- **QR Code** nas faturas

#### 2. **l10n_pt_stock_invoicexpress** - Guias de Transporte
- **Guias de transporte** automáticas para conformidade AT
- **Integração com stock** Odoo
- **Rastreabilidade** de movimentos
- **⚠️ ATENÇÃO LEGAL**: Obrigação AT para TODOS os transportes em território português

#### 3. **l10n_pt_vat**
- **Gestão IVA** específica PT
- **Códigos isenção** AT
- **Normas ajustamento** IVA

### Configuração InvoiceXpress

#### Passo 1: Credenciais API
```
Contabilidade → Configuração → InvoiceXpress
```
- **API Key**: Obtida no painel InvoiceXpress
- **Account Name**: Nome da conta
- **Environment**: Sandbox/Production

#### Passo 2: Mapeamento de Contas
```python
# Configuração automática de:
Conta Vendas PT     → InvoiceXpress Item Type
Conta IVA           → Tax Rate Mapping
Sequência Faturas   → Document Series
```

#### Passo 3: Sincronização
- **Manual**: Botão "Enviar para InvoiceXpress"
- **Automática**: Via cron job (configurável)
- **Webhook**: Notificações em tempo real

### Funcionalidades Específicas

#### SAF-T PT (Standard Audit File for Tax)
- **Exportação automática** para AT
- **Validação** antes envio
- **Histórico** de submissões

#### Faturação Eletrónica
- **PDF** com QR Code obrigatório
- **Assinatura digital** (opcional)
- **Email** automático ao cliente

---

## 🚛 Guias de Transporte - Conformidade Legal AT

### ⚠️ OBRIGAÇÃO LEGAL CRÍTICA

> **🚨 IMPORTANTE**: Segundo a legislação portuguesa (AT), **TODOS** os transportes que ocorram em território português **DEVEM** ter guia de transporte comunicada à AT, **independentemente da nacionalidade do cliente**.

### 📋 Obrigações Legais - Transportes

| Situação | Obrigação Guia AT | Sistema Atual | Status |
|----------|-------------------|---------------|--------|
| **Cliente Português** | ✅ OBRIGATÓRIA | ✅ Gera automaticamente | ✅ CONFORME |
| **Cliente Estrangeiro (em PT)** | ✅ OBRIGATÓRIA | ❌ NÃO gera automaticamente | ⚠️ **PROBLEMÁTICO** |
| **Exportação (desde PT)** | ✅ OBRIGATÓRIA | ❌ NÃO gera automaticamente | ⚠️ **PROBLEMÁTICO** |
| **Transferência Interna** | ✅ OBRIGATÓRIA | ⚙️ Configurável | ⚙️ CONDICIONAL |

### 🔧 Problema Atual do Sistema

**Limitação Identificada:**
```python
# Código atual (INCORRETO para conformidade):
is_PT = not country or country.code == "PT"  # Apenas clientes PT
if pick_doc_type and pick_doc_type != "none" and is_PT:
    pick.invoicexpress_doc_type = pick_doc_type

# Deveria ser (CORRETO para conformidade):
company_is_PT = pick.company_id.country_id.code == "PT"  # Empresa PT
if pick_doc_type and pick_doc_type != "none" and company_is_PT:
    pick.invoicexpress_doc_type = pick_doc_type
```

### ✅ Soluções de Conformidade

#### **Solução 1: Configuração por Tipo de Operação (IMEDIATA)**

1. **Vá a**: `Inventário → Configuração → Tipos de Operação`
2. **Configure TODOS os tipos de saída** com:
   - `InvX Doc Type` = **"Guia de Transporte / Transport"**
   - Ou `InvX Doc Type` = **"Guia de Remessa / Shipping"**
3. **Nunca use** `"No InvoiceXpress document"` para entregas externas

#### **Solução 2: Validação Manual para Clientes Não-PT**

Para **clientes estrangeiros**, até correção do código:

1. **Validar transferência** normalmente
2. **Criar manualmente** a guia:
   - Botão "Create InvoiceXpress" (se disponível)
   - Ou temporariamente alterar país cliente para PT → validar → reverter país
3. **Verificar** que guia foi comunicada à AT

#### **Solução 3: Customização do Módulo (PERMANENTE)**

```python
# Modificação necessária em: 
# vika-addons-custom/l10n_pt_stock_invoicexpress/models/stock_picking.py

def _compute_invoicexpress_doc_type(self):
    for pick in self:
        pick_doc_type = pick.picking_type_id.invoicexpress_doc_type
        
        # CORREÇÃO: Baseada na empresa, não no cliente
        company_country = pick.company_id.country_id
        is_PT_company = not company_country or company_country.code == "PT"
        
        # Gerar guia se empresa é portuguesa (conformidade legal)
        if pick_doc_type and pick_doc_type != "none" and is_PT_company:
            pick.invoicexpress_doc_type = pick_doc_type
```

### 📝 Tipos de Guias Disponíveis

#### 1. **Guia de Transporte** (`"transport"`)
- **Uso**: Transporte de mercadorias vendidas
- **Obrigatoriedade**: Vendas com transporte
- **Código AT**: GT YYYY/NNNN

#### 2. **Guia de Remessa** (`"shipping"`)
- **Uso**: Remessa sem venda (consignação, demonstração)
- **Obrigatoriedade**: Mercadorias não vendidas em movimento
- **Código AT**: GR YYYY/NNNN

#### 3. **Guia de Devolução** (`"devolution"`)
- **Uso**: Devoluções de clientes
- **Obrigatoriedade**: Mercadorias retornadas
- **Código AT**: GD YYYY/NNNN

### 📊 Informações Incluídas na Guia

- **🗓️ Data e hora** de carregamento
- **📅 Data de validade** (padrão: +7 dias)
- **🚗 Matrícula do veículo** (campo obrigatório)
- **📍 Endereços** origem e destino completos
- **📦 Produtos** com quantidades exatas
- **💰 Valores** (podem ser €0,00 para guias)
- **🧾 Impostos** aplicáveis
- **🔗 Referências** origem (ordem venda)

### ⚙️ Configuração Técnica

#### **Empresa (Configuração Geral)**
```
Configurações → Geral → InvoiceXpress → Entregas
```
- ✅ **API Key** configurada
- ✅ **Template email** entregas
- ✅ **Envio automático** ativado

#### **Tipos de Operação**
```
Inventário → Configuração → Tipos de Operação
```
- **Entregas Cliente**: `InvX Doc Type` = `"transport"`
- **Transferências**: `InvX Doc Type` = `"transport"` ou `"none"`
- **Devoluções**: `InvX Doc Type` = `"devolution"`

#### **Campos na Transferência**
- **📋 Tipo Documento**: Automático baseado no tipo operação
- **📧 Enviar Email**: Checkbox para email automático
- **🚗 Matrícula**: Campo obrigatório para conformidade
- **📅 Validade**: Data limite da guia (configurável)

### 🔄 Processo Automático (Cliente PT)

1. **Criar** ordem de venda
2. **Confirmar** entrega
3. **Validar** transferência
4. **Sistema automático**:
   - ✅ Cria guia InvoiceXpress
   - ✅ Comunica à AT
   - ✅ Envia email (se configurado)
   - ✅ Regista número e link no Odoo

### 🔧 Processo Manual (Cliente Não-PT)

1. **Criar** ordem de venda
2. **Confirmar** entrega
3. **Validar** transferência
4. **⚠️ ATENÇÃO**: Sistema não cria automaticamente
5. **Manual**:
   - 🔘 Botão "Create InvoiceXpress"
   - 🔘 Ou alterar temporariamente país cliente
   - 🔘 Verificar criação da guia

### 🚨 Alertas de Não-Conformidade

#### **Situações de Risco:**
- ❌ Cliente estrangeiro sem guia gerada
- ❌ Tipo operação configurado como "none"
- ❌ Transferência validada sem documento AT
- ❌ Campos obrigatórios em branco (matrícula)

#### **Verificações Necessárias:**
```
Inventário → Todas as Operações → Filtrar:
- Estado: "Concluído"
- InvoiceXpress ID: "Vazio"
- Data: Última semana
```

### 📋 Checklist de Conformidade

#### **Diário:**
- [ ] Todas as transferências têm guia gerada
- [ ] Campos obrigatórios preenchidos
- [ ] Links InvoiceXpress funcionais

#### **Mensal:**
- [ ] Audit todas as transferências vs guias AT
- [ ] Verificar clientes estrangeiros
- [ ] Review configurações tipos operação
- [ ] Backup documentos fiscais

### 🔗 Relatórios de Conformidade

#### **Relatório 1: Transferências sem Guia AT**
```sql
-- Query para identificar não-conformidades
SELECT 
    sp.name, 
    sp.partner_id, 
    sp.date_done, 
    sp.invoicexpress_id
FROM stock_picking sp
WHERE sp.state = 'done' 
    AND sp.invoicexpress_id IS NULL
    AND sp.picking_type_code = 'outgoing'
    AND sp.date_done >= current_date - interval '30 days';
```

#### **Relatório 2: Guias Comunicadas à AT**
```
InvoiceXpress → Documentos → Filtrar:
- Tipo: Guias Transporte/Remessa
- Estado: "Comunicado AT"
- Período: Mês atual
```

---

## 💰 Account Asset Management - Gestão de Ativos

### Funcionalidades
- **Cadastro de ativos fixos** completo
- **Depreciação automática** (linear, degressive, manual)
- **Reavaliações** e impairment
- **Baixa de ativos** por venda/sucata
- **Relatórios** de imobilizado

### Tipos de Depreciação

#### 1. **Linear** (Método mais comum)
```
Valor Depreciação = (Custo - Valor Residual) / Vida Útil
```

#### 2. **Degressive** (Accelerated)
```
Taxa = (100% / Vida Útil) × Fator Multiplicador
```

#### 3. **Manual** (Específico por período)
- Inserção manual de valores
- Ideal para ativos únicos

### Configuração de Ativos

#### Passo 1: Categorias de Ativos
```
Contabilidade → Configuração → Asset Categories
```
**Exemplos:**
- **Equipamento Informático**: 3 anos, linear
- **Viaturas**: 4 anos, degressive 
- **Móveis e Utensílios**: 8 anos, linear
- **Edifícios**: 50 anos, linear

#### Passo 2: Contas Contábeis
```python
Conta do Ativo     # 43x - Imobilizações
Conta Depreciação  # 48x - Amortizações Acumuladas  
Conta Gasto        # 66x - Gastos de Depreciação
```

### Fluxo de Trabalho
1. **Criar Ativo**: Desde fatura de fornecedor
2. **Confirmar**: Inicia depreciação automática
3. **Lançamentos**: Gerados mensalmente
4. **Relatórios**: Tracking e compliance

---

## 📊 Account Tax Balance - Balancete Fiscal

### Descrição
Relatório específico para **gestão fiscal** com cálculos automáticos de impostos, base tributável e conformidade regulatória.

### Funcionalidades
- **Mapa resumo IVA** mensal/trimestral
- **Base tributável** por taxa
- **IVA liquidado** vs **IVA dedutível**
- **Apuramento** automático
- **Exportação** para declarações

### Configuração
```
Contabilidade → Relatórios → Tax Balance
```

**Parâmetros:**
- **Período**: Mês/trimestre fiscal
- **Empresa**: Multi-empresa
- **Impostos**: Filtrar por tipos

### Interpretação do Relatório
```
IVA Liquidado (Vendas)    €1.000
IVA Dedutível (Compras)     €300
---------------------------------
IVA a Entregar            €700
```

---

## 👥 Partner Statement - Extratos de Parceiros

### Funcionalidades
- **Extratos de conta corrente** detalhados
- **Saldos em aberto** por vencimento
- **Histórico de pagamentos** completo
- **Envio automático** por email
- **Múltiplos formatos** (PDF, Excel)

### Tipos de Extratos

#### 1. **Statement of Account** - Extrato Simples
- Movimentos chronológicos
- Saldo corrente acumulado
- Ideal para reconciliação

#### 2. **Outstanding Statement** - Em Aberto
- Apenas itens não pagos
- Agrupamento por vencimento
- Cobrança eficiente

#### 3. **Activity Statement** - Atividade
- Todos os movimentos período
- Pagamentos e faturas
- Análise completa

### Configuração e Uso
```
Contabilidade → Relatórios → Partner Statement
```

**Opções:**
- **Parceiros**: Específicos ou todos
- **Data**: Até determinada data
- **Incluir**: Movimentos zerados
- **Layout**: Standard ou personalizado

---

## 📄 Report XLSX - Relatórios Excel

### Módulos
- **report_xlsx**: Base para exportação Excel
- **report_xlsx_helper**: Ferramentas adicionais

### Funcionalidades
- **Formatação avançada** (cores, bordas, gráficos)
- **Fórmulas Excel** nativas
- **Múltiplas abas** por relatório
- **Charts** integrados
- **Pivot tables** automáticas

---

## 📅 Date Range - Períodos Contábeis

### Funcionalidades
- **Períodos fiscais** personalizados
- **Calendário fiscal** português
- **Períodos móveis** (últimos 30 dias, YTD)
- **Comparativos** automáticos
- **Integração** com todos os relatórios

### Configuração de Períodos
```
Contabilidade → Configuração → Date Ranges
```

**Exemplos:**
- **Mensal**: Janeiro 2024, Fevereiro 2024...
- **Trimestral**: Q1 2024, Q2 2024...
- **Anual**: Exercício 2024
- **Móvel**: Últimos 12 meses, YTD

---

## 📝 Account Move Template - Templates de Lançamentos

### Funcionalidades
- **Templates** de lançamentos recorrentes
- **Substituição automática** de variáveis
- **Agendamento** de lançamentos
- **Aprovação** em lote
- **Auditoria** de alterações

### Casos de Uso
- **Salários mensais** automatizados
- **Renda e seguros** recorrentes  
- **Depreciações** automáticas
- **Provisões** regulares
- **Reclassificações** padrão

### Criação de Templates
```
Contabilidade → Configuração → Journal Entry Templates
```

**Variáveis disponíveis:**
- `${date}` - Data atual
- `${user}` - Utilizador atual
- `${company}` - Empresa
- `${amount}` - Valor personalizado

---

## ⚙️ Configuração Inicial Completa

### 1. **Plano de Contas Português**
```
Contabilidade → Configuração → Chart of Accounts
```
- **Importar** SNC (Sistema Normalização Contabilística)
- **Personalizar** contas específicas
- **Ativar** reconciliação onde necessário

### 2. **Impostos Portugueses**
```python
IVA Normal 23%     # Vendas/Compras standard
IVA Intermédio 13% # Restauração, bebidas
IVA Reduzido 6%    # Alimentação, livros
IVA Isento 0%      # Exportações, saúde
```

### 3. **Diários Contábeis**
- **VND**: Vendas (Customer Invoices)
- **CMP**: Compras (Vendor Bills)
- **BCO**: Banco (Bank Statements)
- **CX**: Caixa (Cash)
- **DIV**: Diversos (Miscellaneous)

### 4. **Sequências Documentais**
```
FT 2024/001   # Faturas
NC 2024/001   # Notas Crédito
GR 2024/001   # Guias Receção
GT 2024/001   # Guias Transporte
```

### 5. **Utilizadores e Permissões**
```python
Contabilista      # Full access contabilidade
Gestor Financeiro # Relatórios + aprovações  
Utilizador        # Apenas consulta
Auditor          # Read-only all
```

---

## 📊 Dashboards e KPIs

### Dashboard Principal
**Contabilidade → Dashboards → Financial Overview**

#### KPIs Automáticos:
- **Receitas MTD/YTD** com % crescimento
- **Margem Bruta** e evolução
- **Cash Flow** projetado
- **A/R Aging** - alertas vencidos
- **A/P Aging** - pagamentos pendentes
- **Budget vs Actual** - desvios

#### Gráficos Dinâmicos:
- **Revenue Trend** (12 meses)
- **Expense Breakdown** (por categoria)
- **Profitability Analysis** (por produto/projeto)
- **Cash Position** (histórico + projeção)

---

## 🔧 Resolução de Problemas Comuns

### 1. **Menu Contabilidade não aparece**
```bash
# Verificar módulo account_usability
python odoo-bin -d DATABASE -i account_usability

# Limpar cache browser
Ctrl+F5 ou modo incógnito
```

### 2. **MIS Reports não carregam dados**
```python
# Verificar expressões:
account_balances('4%')     # ✅ Correto
account_balance('4%')      # ❌ Erro função
account_balances('4%%')    # ❌ Erro sintaxe
```

### 3. **InvoiceXpress erro sincronização**
```
# Logs detalhados:
Contabilidade → InvoiceXpress → View Logs

# Verificar:
- API Key válida
- Mapeamento contas
- Formato documentos
```

### 4. **Relatórios Financial Report vazios**
```python
# Verificar filtros:
Data inicial <= Data final
Contas existem no plano
Movimentos contabilizados (não draft)
Utilizador tem permissões
```

### 5. **Performance lenta**
```sql
-- Indexes críticos
CREATE INDEX account_move_line_account_date 
ON account_move_line (account_id, date);

-- Vacuum regular PostgreSQL
VACUUM ANALYZE account_move_line;
```

### 6. **Guias de Transporte não geradas automaticamente**
```python
# Problema: Cliente estrangeiro sem guia AT
# Verificar na transferência:
- Tipo Operação: InvX Doc Type != "none"
- InvoiceXpress ID: vazio após validação
- País cliente: != "PT"

# Solução imediata:
1. Alterar temporariamente país cliente para "PT"
2. Revalidar transferência (se possível)
3. Ou usar botão "Create InvoiceXpress" (se disponível)
4. Reverter país cliente original

# Solução permanente:
Customizar módulo l10n_pt_stock_invoicexpress
- Alterar lógica is_PT para is_PT_company
- Baseada na empresa, não no cliente
```

### 7. **Erro "Missing country" em InvoiceXpress**
```python
# Erro comum: ValidationError missing country
# Verificar campos obrigatórios:

Partner (Cliente):
- ✅ Nome completo
- ✅ País definido (mesmo que ≠ PT) 
- ✅ NIF/VAT (se aplicável)
- ✅ Morada completa

Empresa (Origem):
- ✅ País = "Portugal"
- ✅ NIF português válido
- ✅ Morada sede portuguesa
```

---

## ⭐ Melhores Práticas

### 📋 **Processo Mensal de Fecho**

#### Semana 1:
1. **Reconciliação bancária** completa
2. **Conferência caixa** e fundos
3. **Review A/R** - provisões duvidosos
4. **Review A/P** - accruals pendentes

#### Semana 2:
5. **Depreciações** automáticas (verificar)
6. **Amortizações** diferidos
7. **Provisões** (férias, subsídios)
8. **Reclassificações** curto/longo prazo

#### Semana 3:
9. **Balancete preliminar** 
10. **Análise desvios** budget vs actual
11. **Correções** lançamentos
12. **Review analítica** por projeto/departamento

#### Semana 4:
13. **Demonstrações finais**
14. **MIS Reports** management
15. **Dashboards** atualização
16. **Backup** e arquivo

### 🚛 **Processo de Conformidade - Guias de Transporte**

#### **Verificação Diária:**
1. **Audit transferências** concluídas sem guia AT
2. **Verificar campos** obrigatórios (matrícula, datas)
3. **Confirmar comunicação** AT via InvoiceXpress
4. **Review clientes** estrangeiros processados

#### **Verificação Semanal:**
5. **Relatório não-conformidades** (SQL query fornecida)
6. **Review configurações** tipos de operação
7. **Teste processo** manual para clientes não-PT
8. **Backup documentos** fiscais gerados

#### **Auditoria Mensal:**
9. **Comparativo** transferências vs guias AT
10. **Análise desvios** e correções aplicadas
11. **Update procedimentos** conforme legislação
12. **Formação equipas** sobre conformidade

#### **Checklist Anual:**
13. **Review compliance** legislação AT
14. **Upgrade módulos** português (se disponível)
15. **Auditoria externa** documentação fiscal
16. **Plano contingência** para não-conformidades

---

## 📞 Suporte e Recursos

### 🔗 **Links Úteis**
- **OCA Website**: https://odoo-community.org/
- **MIS Builder Docs**: https://github.com/OCA/mis-builder
- **InvoiceXpress API**: https://invoicexpress.com/api
- **Odoo Documentation**: https://odoo.com/documentation/18.0/

### 📧 **Contactos Suporte**
- **Técnico VIKA**: suporte@vika.pt
- **Emergências**: +351 xxx xxx xxx
- **Formação**: formacao@vika.pt

### 🎓 **Formação Adicional**
1. **Odoo Accounting Basics** (8h)
2. **MIS Builder Advanced** (4h)  
3. **Portuguese Localization** (4h)
4. **Financial Reporting** (6h)
5. **Custom Development** (16h)

---

## 🔄 Atualizações e Roadmap

### 📅 **Próximas Versões**
- **Q1 2025**: Upgrade Odoo 18.1
- **Q2 2025**: SAF-T v2.0 compliance
- **Q3 2025**: AI-powered reconciliation
- **Q4 2025**: Advanced cash flow forecasting

### 🔔 **Change Log**
- **v1.0.0** (Jan 2025): Setup inicial completo
- **v1.1.0** (Jan 2025): ⚠️ **CRÍTICO** - Documentação conformidade guias transporte AT
- **v1.2.0** (Fev 2025): MIS Builder templates
- **v1.3.0** (Mar 2025): InvoiceXpress v2 + correção módulo guias

---

## 📝 Conclusão

O sistema contábil VIKA oferece uma solução completa e robusta para gestão financeira, combinando o melhor do Odoo Community com os módulos especializados da OCA. 

### 🎯 **Pontos-Chave do Sistema:**

1. **✅ Conformidade Legal Total** - InvoiceXpress integrado para obrigações AT
2. **⚠️ Atenção Crítica** - Guias de transporte obrigatórias para TODOS os clientes
3. **📊 Relatórios Avançados** - MIS Builder e Financial Reports para análise
4. **🔧 Customização VIKA** - Módulos adaptados às necessidades específicas

### 🚨 **Alerta de Conformidade:**

> **IMPORTANTE**: O módulo de guias de transporte atual tem uma **limitação crítica** - não gera automaticamente guias para clientes estrangeiros, violando obrigações legais AT. Siga as **soluções propostas** neste manual até correção definitiva do código.

### 📋 **Ações Imediatas Recomendadas:**

1. **Verificar** todas as transferências dos últimos 30 dias
2. **Configurar** tipos de operação com guias obrigatórias  
3. **Implementar** processo manual para clientes não-PT
4. **Planear** customização permanente do módulo

Este manual serve como referência completa para maximizar o uso de todas as funcionalidades disponíveis, garantindo **compliance rigoroso**, eficiência operacional e insights financeiros valiosos para a gestão.

Para dúvidas específicas, formação adicional ou **urgências de conformidade**, contacte a equipa de suporte VIKA.

---

*Última atualização: Janeiro 2025 | Versão: 1.1.0 | VIKA - Soluções Empresariais*

