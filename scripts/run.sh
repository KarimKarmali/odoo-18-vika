#!/bin/bash
# Script para executar Odoo 18 em desenvolvimento
# VK Commodities

echo "🚀 Iniciando Odoo 18 - VK Commodities..."

# Verificar se Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker não está rodando. Inicie o Docker primeiro."
    exit 1
fi

# Parar containers existentes
echo "🛑 Parando containers existentes..."
docker-compose down

# Construir e iniciar
echo "🔨 Construindo e iniciando containers..."
docker-compose up --build -d

# Mostrar logs
echo "📋 Logs do Odoo:"
docker-compose logs -f odoo
