# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManualUtilizador(models.TransientModel):
    _name = 'manual.utilizador'
    _description = 'Manual do Utilizador'

    content = fields.Html('Conteúdo', readonly=True)

    @api.model
    def default_get(self, fields_list):
        result = super().default_get(fields_list)
        
        # Conteúdo HTML do manual
        manual_html = """
        <style>
            body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; color: #333; }
            .manual-section {
                background: white;
                padding: 20px;
                margin-bottom: 15px;
                border-radius: 8px;
                border: 1px solid #dee2e6;
            }
            .manual-highlight {
                background: #e8f4f8;
                padding: 15px;
                border-left: 4px solid #17a2b8;
                margin: 15px 0;
                border-radius: 4px;
            }
            .manual-warning {
                background: #fff3cd;
                padding: 15px;
                border-left: 4px solid #ffc107;
                margin: 15px 0;
                border-radius: 4px;
            }
            .manual-success {
                background: #d4edda;
                padding: 15px;
                border-left: 4px solid #28a745;
                margin: 15px 0;
                border-radius: 4px;
            }
            .manual-danger {
                background: #f8d7da;
                padding: 15px;
                border-left: 4px solid #dc3545;
                margin: 15px 0;
                border-radius: 4px;
            }
            .menu-path {
                background: #f8f9fa;
                padding: 8px 12px;
                border-radius: 4px;
                font-family: monospace;
                border: 1px solid #dee2e6;
                display: inline-block;
                margin: 5px 0;
            }
            .toc {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin-bottom: 20px;
                border: 1px solid #dee2e6;
            }
            .toc ul { margin: 0; padding-left: 20px; }
            .toc li { margin-bottom: 5px; }
            h1 { color: #495057; text-align: center; margin-bottom: 30px; }
            h2 { color: #495057; border-bottom: 2px solid #dee2e6; padding-bottom: 10px; margin-top: 30px; }
            h3 { color: #6c757d; margin-top: 20px; }
            h4 { color: #868e96; }
            code { background: #f8f9fa; padding: 2px 6px; border-radius: 3px; }
            ul li, ol li { margin-bottom: 5px; }
        </style>

        <h1>📖 Manual do Utilizador - Contabilidade VK Commodities</h1>
        
        <div class="toc">
            <h2>📋 Índice</h2>
            <ul>
                <li><a href="#navegacao">🔐 Acesso e Navegação</a></li>
                <li><a href="#modulos">📊 Módulos de Contabilidade</a></li>
                <li><a href="#plano-contas">🏦 Plano de Contas Português</a></li>
                <li><a href="#iva">💰 IVA - Configuração e Mapas</a></li>
                <li><a href="#saft">📄 SAF-T para a AT</a></li>
                <li><a href="#invoicexpress">🔗 InvoiceXpress</a></li>
                <li><a href="#reports">📊 Relatórios Contabilísticos</a></li>
                <li><a href="#reconciliacao">🏦 Reconciliação Bancária</a></li>
                <li><a href="#fecho-mes">📅 Fecho do Mês</a></li>
                <li><a href="#acrescimos">📈 Acréscimos</a></li>
                <li><a href="#transito">🚛 Mercadoria em Trânsito</a></li>
                <li><a href="#mapa-transito">📊 Mapa de Trânsito (Novo!)</a></li>
                <li><a href="#analitica">🎯 Contabilidade Analítica</a></li>
                <li><a href="#centros-custo">🏢 Centros de Custo</a></li>
            </ul>
        </div>

        <div class="manual-section" id="navegacao">
            <h2>🔐 Acesso e Navegação</h2>
            
            <h3>Menu Principal</h3>
            <div class="menu-path">Accounting > Dashboard</div>
            
            <h3>Módulos Disponíveis</h3>
            <ul>
                <li><strong>Dashboard:</strong> Visão geral financeira</li>
                <li><strong>Customers:</strong> Gestão de clientes</li>
                <li><strong>Vendors:</strong> Gestão de fornecedores</li>
                <li><strong>Accounting:</strong> Lançamentos e movimentos</li>
                <li><strong>Reporting:</strong> Relatórios e mapas</li>
                <li><strong>Configuration:</strong> Configurações</li>
            </ul>
        </div>

        <div class="manual-section" id="modulos">
            <h2>📊 Módulos de Contabilidade</h2>
            
            <h3>Sales (Vendas)</h3>
            <ul>
                <li><strong>Quotations:</strong> Orçamentos a clientes</li>
                <li><strong>Orders:</strong> Encomendas confirmadas</li>
                <li><strong>Teams:</strong> Equipas comerciais</li>
                <li><strong>Reporting:</strong> Análise de vendas</li>
            </ul>
            
            <h3>Purchases (Compras)</h3>
            <ul>
                <li><strong>Requests for Quotation:</strong> Pedidos de orçamento</li>
                <li><strong>Purchase Orders:</strong> Ordens de compra</li>
                <li><strong>Vendors:</strong> Gestão de fornecedores</li>
                <li><strong>Products:</strong> Catálogo de produtos</li>
            </ul>
            
            <h3>Inventory (Inventário)</h3>
            <ul>
                <li><strong>Operations:</strong> Movimentos de stock</li>
                <li><strong>Products:</strong> Gestão de artigos</li>
                <li><strong>Reporting:</strong> Relatórios de stock</li>
                <li><strong>Configuration:</strong> Armazéns e localizações</li>
            </ul>
            
            <h3>Invoicing (Faturação)</h3>
            <ul>
                <li><strong>Customer Invoices:</strong> Facturas a clientes</li>
                <li><strong>Vendor Bills:</strong> Facturas de fornecedores</li>
                <li><strong>Payments:</strong> Pagamentos e recebimentos</li>
                <li><strong>Products:</strong> Artigos e preços</li>
            </ul>
        </div>

        <div class="manual-section" id="plano-contas">
            <h2>🏦 Plano de Contas Português</h2>
            
            <h3>Estrutura SNC</h3>
            <ul>
                <li><strong>Classe 1:</strong> Meios Financeiros Líquidos</li>
                <li><strong>Classe 2:</strong> Contas a Receber e a Pagar</li>
                <li><strong>Classe 3:</strong> Inventários e Ativos Biológicos</li>
                <li><strong>Classe 4:</strong> Investimentos</li>
                <li><strong>Classe 5:</strong> Capital, Reservas e Resultados</li>
                <li><strong>Classe 6:</strong> Gastos</li>
                <li><strong>Classe 7:</strong> Rendimentos</li>
                <li><strong>Classe 8:</strong> Resultados</li>
            </ul>
            
            <h3>Contas Principais</h3>
            <ul>
                <li><code>11</code> - Caixa</li>
                <li><code>12</code> - Depósitos Bancários</li>
                <li><code>21</code> - Clientes</li>
                <li><code>22</code> - Fornecedores</li>
                <li><code>31</code> - Mercadorias</li>
                <li><code>36</code> - Mercadoria em Trânsito</li>
                <li><code>61</code> - Custo das Mercadorias</li>
                <li><code>71</code> - Vendas</li>
            </ul>
        </div>

        <div class="manual-section" id="iva">
            <h2>💰 IVA - Configuração e Mapas</h2>
            
            <h3>Taxas de IVA em Portugal</h3>
            <ul>
                <li><strong>23%:</strong> Taxa normal (continente)</li>
                <li><strong>13%:</strong> Taxa intermédia</li>
                <li><strong>6%:</strong> Taxa reduzida</li>
                <li><strong>22%:</strong> Madeira (taxa normal)</li>
                <li><strong>16%:</strong> Açores (taxa normal)</li>
            </ul>
            
            <h3>Códigos de Isenção</h3>
            <ul>
                <li><code>M01</code> - Artigo 16.º n.º 6 do CIVA</li>
                <li><code>M02</code> - Artigo 6.º do DL 198/90</li>
                <li><code>M04</code> - Isenção - Artigo 13.º do CIVA</li>
                <li><code>M05</code> - Isenção - Artigo 14.º do CIVA</li>
                <li><code>M06</code> - Isenção - Artigo 15.º do CIVA</li>
                <li><code>M07</code> - Isenção - Artigo 9.º do CIVA</li>
                <li><code>M09</code> - IVA - não confere direito a dedução</li>
                <li><code>M10</code> - IVA - regime de isenção</li>
                <li><code>M11</code> - Regime particular do tabaco</li>
                <li><code>M12</code> - Regime da margem de lucro - agências viagem</li>
                <li><code>M13</code> - Regime da margem de lucro - objetos de arte</li>
                <li><code>M14</code> - Regime da margem de lucro - metais preciosos</li>
                <li><code>M15</code> - Regime da margem de lucro - objetos usados</li>
                <li><code>M16</code> - Isenção - Artigo 14.º do RITI</li>
                <li><code>M19</code> - Outras isenções</li>
                <li><code>M20</code> - IVA - regime forfetário</li>
                <li><code>M21</code> - IVA - não confere direito a dedução</li>
                <li><code>M25</code> - Mercadorias em consignação</li>
                <li><code>M30</code> - IVA - reverse charge</li>
                <li><code>M31</code> - IVA - reverse charge</li>
                <li><code>M32</code> - IVA - reverse charge</li>
                <li><code>M33</code> - IVA - reverse charge</li>
                <li><code>M40</code> - Isenção - Artigo 6.º do CIVA</li>
                <li><code>M41</code> - Isenção - Artigo 6.º do CIVA</li>
                <li><code>M42</code> - Isenção - Artigo 6.º do CIVA</li>
                <li><code>M43</code> - Isenção - Artigo 6.º do CIVA</li>
                <li><code>M99</code> - Não sujeito; não tributado</li>
            </ul>
            
            <h3>Como Configurar IVA</h3>
            <ol>
                <li><div class="menu-path">Configuration > Taxes</div></li>
                <li>Criar nova taxa ou editar existente</li>
                <li>Definir percentagem e tipo</li>
                <li>Configurar contas contabilísticas</li>
                <li>Associar código de isenção (se aplicável)</li>
            </ol>
            
            <h3>Mapas de IVA</h3>
            <div class="menu-path">Reporting > Tax Report</div>
            <ul>
                <li><strong>Mensal:</strong> Até ao dia 10 do mês seguinte</li>
                <li><strong>Trimestral:</strong> Empresas com volume de negócios < €650,000</li>
                <li><strong>Campos principais:</strong> 40, 41, 42, 43, 44, 45, 46, 47, 48, 49</li>
            </ul>
        </div>

        <div class="manual-section" id="saft">
            <h2>📄 SAF-T para a AT</h2>
            
            <div class="manual-success">
                <strong>🎯 ACESSO:</strong> <code>Accounting > Reporting > SAF-T Export</code>
            </div>
            
            <h3>O que é o SAF-T?</h3>
            <p>Standard Audit File for Tax purposes - Ficheiro normalizado de contabilidade para fins fiscais, obrigatório em Portugal.</p>
            
            <h3>Configuração</h3>
            <ul>
                <li><strong>Periodicidade:</strong> Mensal (obrigatório)</li>
                <li><strong>Prazo:</strong> Até ao dia 25 do mês seguinte</li>
                <li><strong>Formato:</strong> XML</li>
                <li><strong>Empresa:</strong> Verificar dados fiscais completos</li>
                <li><strong>Tipo:</strong> Contabilidade + Faturação</li>
            </ul>
            
            <h3>Processo de Submissão</h3>
            <ol>
                <li>Gerar ficheiro SAF-T no Odoo</li>
                <li>Validar dados (sem erros)</li>
                <li>Aceder ao Portal das Finanças</li>
                <li>Submeter ficheiro XML</li>
                <li>Confirmar receção pela AT</li>
            </ol>
            
            <div class="manual-highlight">
                <strong>✅ HISTÓRICO:</strong> Todos os SAF-T gerados ficam guardados em <code>Accounting > Reporting > SAF-T History</code>
            </div>
        </div>

        <div class="manual-section" id="mapa-transito">
            <h2>📊 Mapa de Mercadoria em Trânsito (Novo!)</h2>
            
            <div class="manual-success">
                <strong>🆕 NOVIDADE:</strong> Relatório especializado para controlo de mercadoria em trânsito desenvolvido especificamente para VK Commodities!
            </div>

            <h3>🎯 Como Aceder</h3>
            <div class="menu-path">Accounting > Reporting > 🚛 Mapa Mercadoria em Trânsito</div>

            <h3>💡 O que Mostra</h3>
            <ul>
                <li>📅 <strong>Todos os movimentos</strong> das contas 36x em tempo real</li>
                <li>🏢 <strong>Fornecedores</strong> com mercadoria pendente</li>
                <li>📦 <strong>Produtos</strong> específicos em trânsito</li>
                <li>💰 <strong>Valores</strong> exatos por movimento</li>
                <li>📄 <strong>Referências</strong> de facturas/documentos</li>
            </ul>

            <h3>🔍 Funcionalidades</h3>
            <ul>
                <li>✅ <strong>Filtro "Com Saldo"</strong> (ativo por defeito)</li>
                <li>✅ <strong>Pesquisa</strong> por fornecedor, produto, referência</li>
                <li>✅ <strong>Agrupamento</strong> por conta, parceiro, produto</li>
                <li>✅ <strong>Export</strong> para Excel nativo</li>
                <li>✅ <strong>Soma automática</strong> de débitos, créditos, saldos</li>
            </ul>

            <h3>📊 Validação vs Balancete</h3>
            <div class="manual-highlight">
                <strong>🔄 PROCESSO SIMPLES:</strong><br>
                1. <code>Accounting > Reporting > Trial Balance</code> - Filtrar contas 36x e anotar valores<br>
                2. <code>Accounting > Reporting > 🚛 Mapa Mercadoria</code> - Verificar soma dos saldos<br>
                3. <strong>Comparar:</strong> ✅ Valores iguais = OK! | ❌ Diferenças = Investigar
            </div>

            <h3>📈 Vantagens</h3>
            <ul>
                <li>⚡ <strong>Tempo real</strong> - sempre atualizado</li>
                <li>🎯 <strong>Específico</strong> - só dados relevantes</li>
                <li>🔍 <strong>Detalhado</strong> - linha por linha</li>
                <li>📊 <strong>Comparável</strong> - facilita validação</li>
                <li>💾 <strong>Exportável</strong> - para análise externa</li>
            </ul>
        </div>

        <div class="manual-section" id="transito">
            <h2>🚛 Mercadoria em Trânsito (Conta 36)</h2>
            
            <h3>O que é Mercadoria em Trânsito?</h3>
            <p>Representa mercadoria <strong>comprada mas ainda não recebida fisicamente</strong>:</p>
            <ul>
                <li>✅ Factura foi emitida pelo fornecedor</li>
                <li>✅ Entrada contabilística foi feita</li>
                <li>❌ Mercadoria ainda não chegou ao armazém</li>
                <li>❌ Entrada em stock ainda não foi processada</li>
            </ul>

            <h3>Movimento Contabilístico Correto</h3>
            <div class="manual-danger">
                <strong>❌ ERRO COMUM:</strong><br>
                • Débito: 61 - Compras €10,000<br>
                • Crédito: 22 - Fornecedores €10,000<br>
                <em>Problema: Mercadoria não chegou, mas contabilidade regista como recebida!</em>
            </div>

            <div class="manual-success">
                <strong>✅ SOLUÇÃO CORRECTA:</strong><br>
                • Débito: 36 - Mercadoria em trânsito €10,000<br>
                • Crédito: 22 - Fornecedores €10,000<br>
                <em>Efeito: Mercadoria registada como "em viagem"</em>
            </div>

            <div class="manual-highlight">
                <strong>🔄 QUANDO MERCADORIA CHEGA:</strong><br>
                • Débito: 31 - Mercadorias €10,000<br>
                • Crédito: 36 - Mercadoria em trânsito €10,000<br>
                <em>Efeito: Transferir de trânsito para stock físico real</em>
            </div>
        </div>

        <div class="manual-section" id="reconciliacao">
            <h2>🏦 Reconciliação Bancária</h2>
            
            <h3>Processo "Picar" Extractos</h3>
            <p>Matching entre movimentos bancários e lançamentos contabilísticos:</p>
            
            <div class="menu-path">Accounting > Bank > Reconciliation</div>
            
            <ol>
                <li><strong>Importar</strong> extracto bancário (CSV, OFX, etc.)</li>
                <li><strong>"Picar"</strong> cada movimento com factura correspondente</li>
                <li><strong>Validar</strong> que saldo bancário = saldo contabilístico</li>
                <li><strong>Confirmar</strong> reconciliação</li>
                <li><strong>Verificar</strong> movimentos não reconciliados</li>
            </ol>

            <div class="manual-warning">
                <strong>⚠️ ATENÇÃO:</strong> O saldo do extracto TEM que bater certo com o ERP!<br>
                Se não bater, investigar diferenças antes de fechar o mês.
            </div>
            
            <h3>Resolução de Problemas</h3>
            <ul>
                <li><strong>Movimento em falta:</strong> Verificar se foi lançado</li>
                <li><strong>Valor diferente:</strong> Confirmar montantes</li>
                <li><strong>Data diferente:</strong> Usar data valor vs data movimento</li>
                <li><strong>Movimento duplicado:</strong> Reverter e re-processar</li>
            </ul>
        </div>

        <div class="manual-section" id="fecho-mes">
            <h2>📅 Fecho do Mês</h2>
            
            <h3>Procedimentos Obrigatórios</h3>
            <ol>
                <li><strong>Reconciliação bancária</strong> completa</li>
                <li><strong>Lançamento de acréscimos</strong> (se aplicável)</li>
                <li><strong>Validação</strong> conta 36 vs mapa trânsito</li>
                <li><strong>Revisão</strong> balancete vs realidade</li>
                <li><strong>Conferência</strong> de clientes e fornecedores</li>
                <li><strong>Validação</strong> de stocks</li>
            </ol>

            <h3>Conta 31 - Saldar ou Não?</h3>
            <div class="manual-highlight">
                <strong>💡 REGRA:</strong> A conta 31 (Mercadorias) NÃO precisa ser saldada mensalmente.<br>
                Representa o valor do stock em armazém e só se altera com entradas/saídas físicas.
            </div>
            
            <h3>Verificações Finais</h3>
            <ul>
                <li><strong>Balancete</strong> equilibrado (débitos = créditos)</li>
                <li><strong>Clientes</strong> sem valores negativos estranhos</li>
                <li><strong>Fornecedores</strong> com valores coerentes</li>
                <li><strong>IVA</strong> calculado corretamente</li>
                <li><strong>Bancos</strong> reconciliados</li>
            </ul>
        </div>

        <div class="manual-section" id="acrescimos">
            <h2>📈 Acréscimos de Custos e Proveitos</h2>
            
            <h3>Quando Usar</h3>
            <p>Para registar custos/proveitos de um mês que só serão facturados no mês seguinte.</p>
            
            <h3>Exemplo Prático</h3>
            <p><em>Energia elétrica de Janeiro será facturada em Fevereiro, mas o custo é de Janeiro.</em></p>

            <h3>Lançamento no Mês (Janeiro)</h3>
            <div class="manual-success">
                <strong>ACRÉSCIMO DE CUSTOS:</strong><br>
                • Débito: 61 - Custos €1,000<br>
                • Crédito: 24 - Acréscimos de Custos €1,000
            </div>

            <h3>Anulação no Mês Seguinte (Fevereiro)</h3>
            <div class="manual-warning">
                <strong>REVERTER ACRÉSCIMO:</strong><br>
                • Débito: 24 - Acréscimos de Custos €1,000<br>
                • Crédito: 61 - Custos €1,000
            </div>

            <p><em>Depois processar a factura real normalmente no mês de Fevereiro.</em></p>
            
            <h3>Acréscimos de Proveitos</h3>
            <div class="manual-success">
                <strong>ACRÉSCIMO DE PROVEITOS:</strong><br>
                • Débito: 27 - Acréscimos de Proveitos €2,000<br>
                • Crédito: 71 - Vendas €2,000
            </div>
        </div>

        <div class="manual-section" id="analitica">
            <h2>🎯 Contabilidade Analítica</h2>
            
            <h3>O que é?</h3>
            <p>Sistema para análise de custos e proveitos por projeto, departamento ou atividade.</p>
            
            <h3>Configuração</h3>
            <ol>
                <li><div class="menu-path">Configuration > Analytic Accounting > Analytic Plans</div></li>
                <li>Criar planos analíticos (ex: Projetos, Departamentos)</li>
                <li>Definir contas analíticas</li>
                <li>Associar a movimentos contabilísticos</li>
            </ol>
            
            <h3>Exemplo de Uso</h3>
            <ul>
                <li><strong>Projeto A:</strong> Todos os custos do Projeto A</li>
                <li><strong>Departamento Vendas:</strong> Custos comerciais</li>
                <li><strong>Centro Lisboa:</strong> Custos da filial de Lisboa</li>
            </ul>
        </div>

        <div class="manual-section" id="centros-custo">
            <h2>🏢 Centros de Custo</h2>
            
            <h3>Implementação</h3>
            <p>Os centros de custo são implementados através da contabilidade analítica.</p>
            
            <h3>Estrutura Sugerida</h3>
            <ul>
                <li><strong>100 - Administração:</strong> Custos administrativos</li>
                <li><strong>200 - Comercial:</strong> Custos de vendas</li>
                <li><strong>300 - Operações:</strong> Custos operacionais</li>
                <li><strong>400 - Logística:</strong> Custos de transporte e armazém</li>
                <li><strong>500 - IT:</strong> Custos informáticos</li>
            </ul>
            
            <h3>Relatórios</h3>
            <div class="menu-path">Reporting > Management > Analytic Reports</div>
            <ul>
                <li><strong>Por Centro:</strong> Custos por departamento</li>
                <li><strong>Por Período:</strong> Evolução temporal</li>
                <li><strong>Comparativo:</strong> Budget vs Real</li>
            </ul>
        </div>

        <div class="manual-section">
            <h2>📞 Suporte e Contactos</h2>
            <p>Para questões específicas ou problemas técnicos, contactar o departamento de IT da VK Commodities.</p>
            
            <div class="manual-highlight">
                <strong>📅 Última atualização:</strong> Agosto 2025<br>
                <strong>📋 Versão:</strong> Odoo 18 VK Commodities<br>
                <strong>🔄 Inclui:</strong> Novo Mapa de Mercadoria em Trânsito<br>
                <strong>📖 Páginas:</strong> Manual completo com todas as funcionalidades
            </div>
        </div>
        """
        
        result['content'] = manual_html
        return result
