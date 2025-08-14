#!/bin/bash
# Script para deploy automático no CapRover
# VK Commodities - Odoo 18

set -e

# Configurações (ajustar conforme seu setup)
CAPROVER_URL="https://captain.yourdomain.com"
APP_NAME="vk-odoo"
CAPROVER_PASSWORD="${CAPROVER_PASSWORD:-your-password}"

echo "🚀 Iniciando deploy para CapRover..."

# Verificar se caprover CLI está instalado
if ! command -v caprover &> /dev/null; then
    echo "❌ CapRover CLI não encontrado. Instalando..."
    npm install -g caprover
fi

# Login no CapRover (se necessário)
echo "🔑 Fazendo login no CapRover..."
caprover login --caproverUrl $CAPROVER_URL --caproverPassword $CAPROVER_PASSWORD

# Deploy da aplicação
echo "📦 Fazendo deploy da aplicação..."
caprover deploy --caproverUrl $CAPROVER_URL --caproverApp $APP_NAME

echo "✅ Deploy concluído com sucesso!"
echo "🌐 Aplicação disponível em: $CAPROVER_URL/app/$APP_NAME"
