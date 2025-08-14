# Script para instalar requisitos de desenvolvimento
# VK Commodities - Odoo 18

Write-Host "Instalando requisitos para desenvolvimento Odoo 18..." -ForegroundColor Green

# Verificar se Python está disponível
$pythonCmd = $null
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} elseif (Test-Path "C:\Users\karim\AppData\Local\Programs\Python\Python312\python.exe") {
    $pythonCmd = "C:\Users\karim\AppData\Local\Programs\Python\Python312\python.exe"
} else {
    Write-Host "Python nao encontrado! Instale Python 3.10+ primeiro." -ForegroundColor Red
    Write-Host "Download: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host "Python encontrado: $pythonCmd" -ForegroundColor Green

# Criar ambiente virtual se não existe
if (!(Test-Path "venv")) {
    Write-Host "Criando ambiente virtual..." -ForegroundColor Blue
    & $pythonCmd -m venv venv
}

# Ativar ambiente virtual
Write-Host "Ativando ambiente virtual..." -ForegroundColor Blue
& ".\venv\Scripts\Activate.ps1"

# Atualizar pip
Write-Host "Atualizando pip..." -ForegroundColor Blue
& $pythonCmd -m pip install --upgrade pip

# Instalar Odoo 18
Write-Host "Instalando Odoo 18..." -ForegroundColor Blue
& $pythonCmd -m pip install odoo==18.0

# Instalar requirements extras
if (Test-Path "requirements.txt") {
    Write-Host "Instalando dependencias extras..." -ForegroundColor Blue
    & $pythonCmd -m pip install -r requirements.txt
}

Write-Host "Instalacao concluida!" -ForegroundColor Green
Write-Host "Para ativar o ambiente: .\venv\Scripts\Activate.ps1" -ForegroundColor Yellow
