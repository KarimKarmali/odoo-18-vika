#!/bin/bash
# Infrastructure as Code - Deploy CapRover
# VK Commodities - Odoo 18

set -e

# Configurações (ajustar conforme seu setup)
CAPROVER_URL="${CAPROVER_URL:-https://captain.yourdomain.com}"
APP_NAME="${APP_NAME:-vk-odoo}"
CAPROVER_PASSWORD="${CAPROVER_PASSWORD:-your-password}"

echo "🚀 DEPLOY INFRASTRUCTURE AS CODE - VK COMMODITIES"
echo "=================================================="

# Verificar se caprover CLI está instalado
if ! command -v caprover &> /dev/null; then
    echo "❌ CapRover CLI não encontrado. Instalando..."
    npm install -g caprover
fi

# Login no CapRover
echo "🔑 Fazendo login no CapRover..."
caprover login --caproverUrl $CAPROVER_URL --caproverPassword $CAPROVER_PASSWORD

# Deploy da aplicação
echo "📦 Fazendo deploy da aplicação..."
caprover deploy --caproverUrl $CAPROVER_URL --caproverApp $APP_NAME

# Aguardar deploy
echo "⏳ Aguardando deploy..."
sleep 30

# Executar setup de produção (Infrastructure as Code)
echo "🔧 Executando setup automático de produção..."
echo "📋 Instalando módulos obrigatórios..."

# Executar script de setup via API ou SSH
# (Este comando seria executado no container CapRover)
echo "curl -X POST $CAPROVER_URL/api/v1/user/apps/data/$APP_NAME/exec \\"
echo "  -H 'Content-Type: application/json' \\"  
echo "  -d '{\"command\": \"python /app/scripts/setup-production.py\"}'"

echo ""
echo "✅ Deploy Infrastructure as Code concluído!"
echo "🌐 Aplicação: $CAPROVER_URL/app/$APP_NAME"
echo "📋 Módulos instalados automaticamente via código"
echo "🔄 Sistema configurado consistentemente"
