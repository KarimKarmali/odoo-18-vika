# Script PowerShell para criar menu "Manual PT" no Odoo
# VIKA - Manual de Contabilidade

$odooUrl = "http://localhost:8069"
$database = "vika_odoo18"
$username = "admin"
$password = "admin"

Write-Host "🎯 Criando menu 'Manual PT' no Odoo..." -ForegroundColor Green

try {
    # 1. Autenticar no Odoo
    Write-Host "📡 Conectando ao Odoo..." -ForegroundColor Yellow
    
    $authBody = @{
        jsonrpc = "2.0"
        method = "call"
        params = @{
            service = "common"
            method = "authenticate"
            args = @($database, $username, $password, @{})
        }
    } | ConvertTo-Json -Depth 10

    $authResponse = Invoke-RestMethod -Uri "$odooUrl/jsonrpc" -Method Post -Body $authBody -ContentType "application/json"
    
    if ($authResponse.result) {
        $uid = $authResponse.result
        Write-Host "✅ Autenticado com sucesso! UID: $uid" -ForegroundColor Green
    } else {
        Write-Host "❌ Erro na autenticação!" -ForegroundColor Red
        exit 1
    }

    # 2. Procurar o menu pai "Reporting"
    Write-Host "🔍 Procurando menu pai 'Reporting'..." -ForegroundColor Yellow
    
    $searchMenuBody = @{
        jsonrpc = "2.0"
        method = "call"
        params = @{
            service = "object"
            method = "execute_kw"
            args = @(
                $database,
                $uid,
                $password,
                "ir.ui.menu",
                "search",
                @(@(
                    @("name", "=", "Reporting")
                )),
                @{}
            )
        }
    } | ConvertTo-Json -Depth 10

    $menuSearchResponse = Invoke-RestMethod -Uri "$odooUrl/jsonrpc" -Method Post -Body $searchMenuBody -ContentType "application/json"
    
    if ($menuSearchResponse.result -and $menuSearchResponse.result.Count -gt 0) {
        $parentMenuId = $menuSearchResponse.result[0]
        Write-Host "✅ Menu 'Reporting' encontrado! ID: $parentMenuId" -ForegroundColor Green
    } else {
        Write-Host "❌ Menu 'Reporting' não encontrado!" -ForegroundColor Red
        exit 1
    }

    # 3. Criar ação URL
    Write-Host "🔧 Criando ação URL..." -ForegroundColor Yellow
    
    $createActionBody = @{
        jsonrpc = "2.0"
        method = "call"
        params = @{
            service = "object"
            method = "execute_kw"
            args = @(
                $database,
                $uid,
                $password,
                "ir.actions.act_url",
                "create",
                @(@{
                    name = "Manual de Contabilidade VIKA"
                    url = "/account_usability/static/description/manual_contabilidade.html"
                    target = "new"
                }),
                @{}
            )
        }
    } | ConvertTo-Json -Depth 10

    $actionResponse = Invoke-RestMethod -Uri "$odooUrl/jsonrpc" -Method Post -Body $createActionBody -ContentType "application/json"
    
    if ($actionResponse.result) {
        $actionId = $actionResponse.result
        Write-Host "✅ Ação criada com sucesso! ID: $actionId" -ForegroundColor Green
    } else {
        Write-Host "❌ Erro ao criar ação!" -ForegroundColor Red
        Write-Host $actionResponse.error -ForegroundColor Red
        exit 1
    }

    # 4. Criar menu "Manual PT"
    Write-Host "📖 Criando menu 'Manual PT'..." -ForegroundColor Yellow
    
    $createMenuBody = @{
        jsonrpc = "2.0"
        method = "call"
        params = @{
            service = "object"
            method = "execute_kw"
            args = @(
                $database,
                $uid,
                $password,
                "ir.ui.menu",
                "create",
                @(@{
                    name = "📖 Manual PT"
                    parent_id = $parentMenuId
                    action = "ir.actions.act_url,$actionId"
                    sequence = 1
                    web_icon = "fa-book"
                }),
                @{}
            )
        }
    } | ConvertTo-Json -Depth 10

    $menuResponse = Invoke-RestMethod -Uri "$odooUrl/jsonrpc" -Method Post -Body $createMenuBody -ContentType "application/json"
    
    if ($menuResponse.result) {
        $menuId = $menuResponse.result
        Write-Host "🎉 Menu 'Manual PT' criado com sucesso!" -ForegroundColor Green
        Write-Host "📋 Detalhes:" -ForegroundColor Cyan
        Write-Host "   - Menu ID: $menuId" -ForegroundColor White
        Write-Host "   - Action ID: $actionId" -ForegroundColor White
        Write-Host "   - Parent Menu ID: $parentMenuId" -ForegroundColor White
        Write-Host "   - URL: /account_usability/static/description/manual_contabilidade.html" -ForegroundColor White
        Write-Host ""
        Write-Host "✅ O menu está agora disponível em:" -ForegroundColor Green
        Write-Host "   Contabilidade → Reporting → 📖 Manual PT" -ForegroundColor White
        Write-Host ""
        Write-Host "🌐 Acesse: http://localhost:8069" -ForegroundColor Cyan
    } else {
        Write-Host "❌ Erro ao criar menu!" -ForegroundColor Red
        Write-Host $menuResponse.error -ForegroundColor Red
        exit 1
    }

} catch {
    Write-Host "❌ Erro geral: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host $_.Exception -ForegroundColor Red
}

Write-Host ""
Write-Host "🚀 Script concluído! Recarregue a página do Odoo para ver o novo menu." -ForegroundColor Green

