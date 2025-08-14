# Script para corrigir problemas de instalação do mis_builder
# VK Commodities

Write-Host "=== CORREÇÃO MIS_BUILDER ===" -ForegroundColor Green
Write-Host ""

Write-Host "🔧 Aplicando correções..." -ForegroundColor Yellow

# 1. Verificar se as correções foram aplicadas
$manifestPath = "addons\oca\date_range\__manifest__.py"
$manifest = Get-Content $manifestPath -Raw

if ($manifest -match "# ""data/ir_cron_data.xml""") {
    Write-Host "✅ Correção no manifesto aplicada" -ForegroundColor Green
} else {
    Write-Host "❌ Correção no manifesto NÃO aplicada" -ForegroundColor Red
    Write-Host "💡 Execute primeiro a correção manual" -ForegroundColor Yellow
    exit 1
}

# 2. Verificar arquivo de dados
$cronPath = "addons\oca\date_range\data\ir_cron_data.xml"
$cronData = Get-Content $cronPath -Raw

if ($cronData -match "<!-- Cron job temporariamente desabilitado") {
    Write-Host "✅ Arquivo de cron corrigido" -ForegroundColor Green
} else {
    Write-Host "❌ Arquivo de cron NÃO corrigido" -ForegroundColor Red
}

Write-Host ""
Write-Host "=== PRÓXIMOS PASSOS ===" -ForegroundColor Green
Write-Host "1. Vá para o Odoo em Developer Mode" -ForegroundColor White
Write-Host "2. Database Structure > Update Module List" -ForegroundColor White
Write-Host "3. Vá em Apps > Remover filtros" -ForegroundColor White
Write-Host "4. Procure date_range e instale primeiro" -ForegroundColor White
Write-Host "5. Depois procure mis_builder e instale" -ForegroundColor White
Write-Host ""
Write-Host "⚠️  Se ainda der erro, reinicie o Odoo completamente" -ForegroundColor Yellow
Write-Host "⚠️  O cron do date_range foi desabilitado temporariamente" -ForegroundColor Yellow
