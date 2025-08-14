# Script para executar Odoo 18 com Python (sem Docker)
# VK Commodities

Write-Host "Iniciando Odoo 18 com Python - VK Commodities..." -ForegroundColor Green

# Verificar se ambiente virtual existe
if (!(Test-Path "venv")) {
    Write-Host "Ambiente virtual nao encontrado!" -ForegroundColor Red
    Write-Host "Execute primeiro: .\scripts\install-requirements.ps1" -ForegroundColor Yellow
    exit 1
}

# Verificar se Python está disponível
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} else {
    Write-Host "Python nao encontrado!" -ForegroundColor Red
    exit 1
}

# Ativar ambiente virtual
Write-Host "Ativando ambiente virtual..." -ForegroundColor Blue
& ".\venv\Scripts\Activate.ps1"

# Criar diretório de dados se não existe
if (!(Test-Path "data")) {
    New-Item -ItemType Directory -Path "data" -Force | Out-Null
}

# Verificar se PostgreSQL está rodando
Write-Host "Verificando PostgreSQL..." -ForegroundColor Yellow
try {
    $pgCheck = Test-NetConnection -ComputerName localhost -Port 5432 -WarningAction SilentlyContinue
    if (-not $pgCheck.TcpTestSucceeded) {
        Write-Host "PostgreSQL nao esta rodando na porta 5432!" -ForegroundColor Red
        Write-Host "Instale e inicie PostgreSQL primeiro." -ForegroundColor Yellow
        exit 1
    }
    Write-Host "PostgreSQL OK" -ForegroundColor Green
} catch {
    Write-Host "Erro ao verificar PostgreSQL. Certifique-se que esta instalado e rodando." -ForegroundColor Red
    exit 1
}

# Executar Odoo
Write-Host "Iniciando Odoo 18..." -ForegroundColor Green
Write-Host "URL: http://localhost:8069" -ForegroundColor Cyan
Write-Host "Master Password: admin123" -ForegroundColor Cyan
Write-Host "Database: vk_dev" -ForegroundColor Cyan
Write-Host "Pressione Ctrl+C para parar" -ForegroundColor Yellow

python ./odoo-source/odoo-bin -c config/odoo-python.conf -d vk_dev --dev=all
