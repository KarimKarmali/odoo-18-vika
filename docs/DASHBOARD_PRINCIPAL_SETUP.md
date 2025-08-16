# Dashboard Principal VK Commodities - Guia de Configuração

## 🎯 Objetivo
Criar um dashboard principal com ícones das aplicações instaladas para facilitar a navegação no Odoo.

## 📋 Pré-requisitos
- ✅ Odoo 18 em funcionamento
- ✅ Módulo `ks_dashboard_ninja` instalado
- ✅ Acesso de administrador ao sistema

## 🚀 Configuração Passo-a-Passo

### 1. Aceder ao Dashboard Ninja
1. Abrir o navegador e ir para `http://localhost:8069`
2. Fazer login como administrador
3. No menu principal, procurar por **"Dashboard Ninja"** ou **"Dashboards"**
4. Clicar em **"Dashboard Ninja"** > **"Dashboard"**

### 2. Criar Novo Dashboard
1. Clicar no botão **"Criar"** ou **"New"**
2. Preencher os campos:
   - **Nome**: `VK Commodities - Dashboard Principal`
   - **Nome do Menu**: `Dashboard Principal`
   - **Menu Superior**: Selecionar um menu apropriado (ex: "Administração")
   - **Ativo**: ✅ Marcar como ativo

### 3. Configurar Widgets das Aplicações

#### Widget 1: Contabilidade
- **Tipo**: Tile (Azulejo)
- **Nome**: `Contabilidade`
- **Ícone**: `fa-calculator`
- **Cor de Fundo**: `#875A7B`
- **Cor da Fonte**: `#FFFFFF`
- **Informação**: `Gestão financeira e contabilística`
- **Ação**: Configurar para abrir o menu de Contabilidade

#### Widget 2: Vendas
- **Tipo**: Tile (Azulejo)
- **Nome**: `Vendas`
- **Ícone**: `fa-shopping-cart`
- **Cor de Fundo**: `#1f77b4`
- **Cor da Fonte**: `#FFFFFF`
- **Informação**: `Gestão de vendas e orçamentos`
- **Ação**: Configurar para abrir o menu de Vendas

#### Widget 3: Compras
- **Tipo**: Tile (Azulejo)
- **Nome**: `Compras`
- **Ícone**: `fa-shopping-bag`
- **Cor de Fundo**: `#ff7f0e`
- **Cor da Fonte**: `#FFFFFF`
- **Informação**: `Gestão de compras e fornecedores`
- **Ação**: Configurar para abrir o menu de Compras

#### Widget 4: Inventário
- **Tipo**: Tile (Azulejo)
- **Nome**: `Inventário`
- **Ícone**: `fa-cubes`
- **Cor de Fundo**: `#2ca02c`
- **Cor da Fonte**: `#FFFFFF`
- **Informação**: `Gestão de stock e armazém`
- **Ação**: Configurar para abrir o menu de Inventário

#### Widget 5: Discussões
- **Tipo**: Tile (Azulejo)
- **Nome**: `Discussões`
- **Ícone**: `fa-comments`
- **Cor de Fundo**: `#d62728`
- **Cor da Fonte**: `#FFFFFF`
- **Informação**: `Mensagens e comunicação`
- **Ação**: Configurar para abrir o menu de Discussões

#### Widget 6: Relatórios Financeiros
- **Tipo**: Tile (Azulejo)
- **Nome**: `Relatórios Financeiros`
- **Ícone**: `fa-line-chart`
- **Cor de Fundo**: `#9467bd`
- **Cor da Fonte**: `#FFFFFF`
- **Informação**: `Relatórios e análises financeiras`
- **Ação**: Configurar para abrir os relatórios do Base Accounting Kit

### 4. Adicionar KPIs de Gestão

#### KPI 1: Vendas do Mês
- **Tipo**: KPI
- **Nome**: `Vendas do Mês`
- **Modelo**: `sale.order`
- **Campo de Medida**: `amount_total`
- **Domínio**: `[('state','in',['sale','done']),('date_order','>=',datetime.now().replace(day=1))]`
- **Ícone**: `fa-euro`
- **Cor**: `#1f77b4`

#### KPI 2: Compras do Mês
- **Tipo**: KPI
- **Nome**: `Compras do Mês`
- **Modelo**: `purchase.order`
- **Campo de Medida**: `amount_total`
- **Domínio**: `[('state','in',['purchase','done']),('date_order','>=',datetime.now().replace(day=1))]`
- **Ícone**: `fa-shopping-bag`
- **Cor**: `#ff7f0e`

#### KPI 3: Faturas em Aberto
- **Tipo**: KPI
- **Nome**: `Faturas em Aberto`
- **Modelo**: `account.move`
- **Campo de Medida**: `amount_residual`
- **Domínio**: `[('move_type','=','out_invoice'),('payment_state','!=','paid')]`
- **Ícone**: `fa-file-text`
- **Cor**: `#d62728`

### 5. Configurar Layout
1. Usar o modo de edição para organizar os widgets
2. Posicionar os tiles das aplicações na parte superior
3. Colocar os KPIs na parte inferior
4. Ajustar o tamanho dos widgets conforme necessário

### 6. Definir como Página Principal
1. Ir para **Configurações** > **Utilizadores & Empresas** > **Utilizadores**
2. Editar o utilizador administrador
3. Na aba **Preferências**, definir:
   - **Ação de Início**: Selecionar o dashboard criado
   - **Menu de Início**: Dashboard Principal

### 7. Configurar Permissões
1. Ir para **Configurações** > **Utilizadores & Empresas** > **Grupos**
2. Adicionar o dashboard aos grupos apropriados
3. Garantir que todos os utilizadores têm acesso ao dashboard

## 🎨 Personalização Adicional

### Cores VK Commodities
- **Primária**: `#875A7B` (Roxo)
- **Secundária**: `#1f77b4` (Azul)
- **Sucesso**: `#2ca02c` (Verde)
- **Aviso**: `#ff7f0e` (Laranja)
- **Erro**: `#d62728` (Vermelho)

### Ícones FontAwesome Sugeridos
- Contabilidade: `fa-calculator`, `fa-money`, `fa-euro`
- Vendas: `fa-shopping-cart`, `fa-line-chart`, `fa-handshake-o`
- Compras: `fa-shopping-bag`, `fa-truck`, `fa-inbox`
- Inventário: `fa-cubes`, `fa-warehouse`, `fa-boxes`
- Relatórios: `fa-bar-chart`, `fa-pie-chart`, `fa-table`

## 🔧 Resolução de Problemas

### Dashboard não aparece
1. Verificar se o módulo `ks_dashboard_ninja` está instalado
2. Confirmar que o dashboard está marcado como "Ativo"
3. Verificar permissões do utilizador

### Widgets não funcionam
1. Verificar se os modelos referenciados existem
2. Confirmar que os campos de medida estão corretos
3. Testar os domínios de filtro

### Ações não redirecionam
1. Verificar se as ações estão configuradas corretamente
2. Confirmar que os menus de destino existem
3. Testar as permissões de acesso

## 📱 Resultado Final
O dashboard principal incluirá:
- ✅ Navegação visual com ícones das aplicações
- ✅ KPIs em tempo real de vendas, compras e finanças
- ✅ Interface intuitiva e moderna
- ✅ Cores personalizadas VK Commodities
- ✅ Acesso rápido a todas as funcionalidades principais

## 🚀 Próximos Passos
1. Testar o dashboard com diferentes utilizadores
2. Ajustar permissões conforme necessário
3. Adicionar mais KPIs específicos do negócio
4. Configurar atualizações automáticas dos dados
5. Treinar utilizadores na nova interface
