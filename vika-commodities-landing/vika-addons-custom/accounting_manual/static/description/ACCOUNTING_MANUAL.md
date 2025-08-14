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

#### 2. **l10n_pt_stock_invoicexpress**
- **Guias de transporte** automáticas
- **Integração com stock** Odoo
- **Rastreabilidade** de movimentos

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

### Configuração para Desenvolvedores
```python
from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx

class CustomFinancialReport(ReportXlsx):
    def generate_xlsx_report(self, workbook, data, objects):
        # Configurar folha de cálculo
        worksheet = workbook.add_worksheet('Demonstração Resultados')
        
        # Definir formatos
        bold = workbook.add_format({'bold': True})
        money = workbook.add_format({'num_format': '#,##0.00'})
        
        # Escrever dados
        worksheet.write('A1', 'RECEITAS', bold)
        worksheet.write('B1', objects.revenue, money)
```

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

## 🔄 Account Fiscal Year - Exercício Fiscal

### Funcionalidades
- **Exercícios fiscais** personalizados
- **Calendário** não-standard (ex: Abril-Março)
- **Períodos especiais** (13º período)
- **Encerramento** de contas
- **Abertura** novo exercício

### Configuração
```
Contabilidade → Configuração → Fiscal Years
```

**Portugal Standard:**
- **Início**: 1 Janeiro
- **Fim**: 31 Dezembro
- **Períodos**: 12 mensais

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

### Configuração Dashboards
```python
# Widget personalizado exemplo:
{
    'type': 'chart',
    'title': 'Receitas por Mês',
    'data_source': 'account.move.line',
    'domain': [('account_id.user_type_id.type', '=', 'income')],
    'group_by': 'date:month',
    'measure': 'balance'
}
```

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

### 💡 **Otimizações de Performance**

#### Database:
```sql
-- Manutenção regular
REINDEX TABLE account_move_line;
ANALYZE account_move_line;

-- Particionamento por ano (grandes volumes)
CREATE TABLE account_move_line_2024 
PARTITION OF account_move_line 
FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
```

#### Odoo:
```python
# Configuração odoo.conf
db_maxconn = 64
limit_memory_hard = 2684354560  # 2.5GB
limit_memory_soft = 2147483648  # 2GB
workers = 4
max_cron_threads = 2
```

### 🔒 **Segurança e Compliance**

#### Backup Strategy:
```bash
# Backup diário automatizado
pg_dump vika_odoo18 | gzip > backup_$(date +%Y%m%d).sql.gz

# Retention: 30 dias local, 12 meses cloud
find /backups -name "*.sql.gz" -mtime +30 -delete
```

#### Auditoria:
- **Mail tracking** todas comunicações
- **User access logs** detalhados  
- **Document versioning** críticos
- **Approval workflows** configurados
- **Segregation of duties** implementada

#### GDPR Compliance:
```python
# Anonimização dados clientes
# Configurar retenção automática
# Logs acesso dados pessoais
# Exportação dados pedido
```

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
- **v1.1.0** (Fev 2025): MIS Builder templates
- **v1.2.0** (Mar 2025): InvoiceXpress v2

---

## 📝 Conclusão

O sistema contábil VIKA oferece uma solução completa e robusta para gestão financeira, combinando o melhor do Odoo Community com os módulos especializados da OCA. 

Este manual serve como referência completa para maximizar o uso de todas as funcionalidades disponíveis, garantindo compliance, eficiência e insights financeiros valiosos para a gestão.

Para dúvidas específicas ou formação adicional, contacte a equipa de suporte VIKA.

---

*Última atualização: Janeiro 2025 | Versão: 1.0.0 | VIKA - Soluções Empresariais*

