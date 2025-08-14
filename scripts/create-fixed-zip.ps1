# Script para criar ZIP corrigido do mis_builder
Write-Host "Criando ZIP corrigido do MIS Builder..." -ForegroundColor Green

# Criar diretório temporário
$tempDir = "temp_mis_builder_fixed"
if (Test-Path $tempDir) {
    Remove-Item $tempDir -Recurse -Force
}

# Copiar mis_builder corrigido
Copy-Item "addons\oca\mis_builder" $tempDir -Recurse

# Verificar se arquivo problemático existe
$cronFile = "$tempDir\data\ir_cron_data.xml"
if (Test-Path $cronFile) {
    Write-Host "Removendo arquivo problemático..." -ForegroundColor Yellow
    Remove-Item $cronFile -Force
}

# Criar ZIP
$zipPath = "mis_builder_fixed.zip"
if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

Compress-Archive -Path "$tempDir\*" -DestinationPath $zipPath

# Limpar
Remove-Item $tempDir -Recurse -Force

Write-Host "ZIP corrigido criado: $zipPath" -ForegroundColor Green
Write-Host "Use este ZIP para upload no Odoo" -ForegroundColor Cyan
