# Script final de verificação
Write-Host "=== VERIFICACAO FINAL ===" -ForegroundColor Green
Write-Host ""

# Verificar arquivo problemático
if (Test-Path "addons\oca\date_range\data\ir_cron_data.xml.disabled") {
    Write-Host "✅ Arquivo problemático desabilitado" -ForegroundColor Green
} else {
    Write-Host "❌ Arquivo ainda ativo" -ForegroundColor Red
}

# Verificar hook
if (Test-Path "addons\oca\date_range\hooks.py") {
    Write-Host "✅ Post-init hook criado" -ForegroundColor Green
} else {
    Write-Host "❌ Hook não encontrado" -ForegroundColor Red
}

# Verificar manifesto
$manifest = Get-Content "addons\oca\date_range\__manifest__.py" -Raw
if ($manifest -match "post_init_hook") {
    Write-Host "✅ Hook configurado no manifesto" -ForegroundColor Green
} else {
    Write-Host "❌ Hook não configurado" -ForegroundColor Red
}

Write-Host ""
Write-Host "AGORA PODE INSTALAR:" -ForegroundColor Yellow
Write-Host "1. Update Module List"
Write-Host "2. Instalar Date Range"
Write-Host "3. Instalar MIS Builder"
Write-Host ""
Write-Host "O cron será criado automaticamente após instalação!" -ForegroundColor Cyan
