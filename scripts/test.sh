#!/bin/bash
# Script para executar testes do Odoo
# VK Commodities

echo "🧪 Executando testes Odoo 18..."

# Verificar se containers estão rodando
if ! docker-compose ps | grep -q "Up"; then
    echo "❌ Containers não estão rodando. Execute ./scripts/run.sh primeiro."
    exit 1
fi

# Executar testes
if [ -z "$1" ]; then
    echo "📋 Executando todos os testes dos addons customizados..."
    docker-compose exec odoo odoo -c /etc/odoo/odoo.conf -d test_db --test-enable --stop-after-init --addons-path=/opt/odoo/addons/custom
else
    echo "📋 Executando testes do addon: $1"
    docker-compose exec odoo odoo -c /etc/odoo/odoo.conf -d test_db --test-enable --stop-after-init -i $1
fi

echo "✅ Testes concluídos!"
