# Script de diagnóstico para mis_builder
# VK Commodities

Write-Host "=== DIAGNÓSTICO MIS_BUILDER ===" -ForegroundColor Green
Write-Host ""

# Verificar se módulo existe
if (Test-Path "addons\oca\mis_builder\__manifest__.py") {
    Write-Host "✅ Módulo mis_builder encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ Módulo mis_builder NÃO encontrado" -ForegroundColor Red
    exit 1
}

# Verificar dependências
$dependencies = @("report_xlsx", "date_range")
foreach ($dep in $dependencies) {
    if (Test-Path "addons\oca\$dep\__manifest__.py") {
        Write-Host "✅ Dependência $dep encontrada" -ForegroundColor Green
    } else {
        Write-Host "❌ Dependência $dep NÃO encontrada" -ForegroundColor Red
    }
}

# Verificar manifesto
Write-Host ""
Write-Host "📄 Verificando manifesto..." -ForegroundColor Cyan
$manifest = Get-Content "addons\oca\mis_builder\__manifest__.py" -Raw
if ($manifest -match '"installable":\s*True') {
    Write-Host "✅ Módulo marcado como installable" -ForegroundColor Green
} else {
    Write-Host "❌ Módulo NÃO marcado como installable" -ForegroundColor Red
}

if ($manifest -match '"application":\s*True') {
    Write-Host "✅ Módulo marcado como application" -ForegroundColor Green
} else {
    Write-Host "⚠️ Módulo NÃO marcado como application" -ForegroundColor Yellow
}

# Verificar se Docker está rodando
Write-Host ""
Write-Host "🐳 Verificando Docker..." -ForegroundColor Cyan
try {
    docker info | Out-Null
    Write-Host "✅ Docker está rodando" -ForegroundColor Green
    
    # Verificar containers
    $containers = docker-compose ps
    if ($containers -match "Up") {
        Write-Host "✅ Containers Odoo estão rodando" -ForegroundColor Green
        Write-Host "🌐 Acesse: http://localhost:8069" -ForegroundColor Yellow
    } else {
        Write-Host "❌ Containers Odoo NÃO estão rodando" -ForegroundColor Red
        Write-Host "💡 Execute: .\scripts\run.ps1" -ForegroundColor Yellow
    }
} catch {
    Write-Host "❌ Docker NÃO está rodando" -ForegroundColor Red
    Write-Host "💡 Inicie o Docker Desktop primeiro" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "=== PRÓXIMOS PASSOS ===" -ForegroundColor Green
Write-Host "1. Inicie o Docker Desktop" -ForegroundColor White
Write-Host "2. Execute: .\scripts\run.ps1" -ForegroundColor White  
Write-Host "3. Acesse: http://localhost:8069" -ForegroundColor White
Write-Host "4. Vá em Apps > Remover filtros > Procurar 'MIS Builder'" -ForegroundColor White
Write-Host "5. Se não aparecer: Developer Mode > Update Module List" -ForegroundColor White
