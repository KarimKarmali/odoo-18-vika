# Script PowerShell para executar Odoo 18 em desenvolvimento
# VK Commodities

Write-Host "Iniciando Odoo 18 - VK Commodities..." -ForegroundColor Green

# Verificar se Docker esta rodando
try {
    docker info | Out-Null
    Write-Host "Docker esta rodando" -ForegroundColor Green
} catch {
    Write-Host "Docker nao esta rodando. Inicie o Docker primeiro." -ForegroundColor Red
    exit 1
}

# Parar containers existentes
Write-Host "Parando containers existentes..." -ForegroundColor Yellow
docker-compose down

# Construir e iniciar
Write-Host "Construindo e iniciando containers..." -ForegroundColor Blue
docker-compose up --build -d

# Aguardar alguns segundos
Start-Sleep -Seconds 5

# Mostrar status
Write-Host "Status dos containers:" -ForegroundColor Cyan
docker-compose ps

Write-Host "Odoo estara disponivel em: http://localhost:8069" -ForegroundColor Green
Write-Host "Para ver logs: docker-compose logs -f odoo" -ForegroundColor Yellow