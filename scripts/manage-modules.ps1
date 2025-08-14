# Script para gerenciar módulos Odoo
# VK Commodities

param(
    [string]$Action = "help"
)

Write-Host "=== GERENCIADOR DE MÓDULOS ODOO 18 ===" -ForegroundColor Green
Write-Host ""

switch ($Action.ToLower()) {
    "help" {
        Write-Host "USO: .\scripts\manage-modules.ps1 [acao]" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "AÇÕES:" -ForegroundColor Cyan
        Write-Host "  list     - Listar módulos instalados"
        Write-Host "  custom   - Criar novo módulo customizado"  
        Write-Host "  copy     - Copiar módulo instalado para versionamento"
        Write-Host "  status   - Ver status dos módulos"
        Write-Host ""
        Write-Host "EXEMPLOS:" -ForegroundColor Cyan
        Write-Host "  .\scripts\manage-modules.ps1 list"
        Write-Host "  .\scripts\manage-modules.ps1 custom"
        Write-Host "  .\scripts\manage-modules.ps1 copy"
    }
    
    "list" {
        Write-Host "MÓDULOS INSTALADOS NA DATABASE:" -ForegroundColor Yellow
        
        # Ativar ambiente virtual
        & ".\venv\Scripts\Activate.ps1"
        
        # Listar módulos instalados
        python -c "
import psycopg2
try:
    conn = psycopg2.connect(
        host='localhost',
        database='vk_dev', 
        user='odoo',
        password='odoo'
    )
    cur = conn.cursor()
    cur.execute(\"SELECT name, state FROM ir_module_module WHERE state = 'installed' ORDER BY name\")
    modules = cur.fetchall()
    
    print('\\nMÓDULOS INSTALADOS:')
    print('=' * 40)
    for name, state in modules:
        print(f'  ✅ {name}')
    
    print(f'\\nTotal: {len(modules)} módulos instalados')
    
    cur.close()
    conn.close()
except Exception as e:
    print(f'Erro: {e}')
    print('Certifique-se que PostgreSQL esta rodando e database existe.')
"
    }
    
    "custom" {
        Write-Host "CRIAR NOVO MÓDULO CUSTOMIZADO:" -ForegroundColor Yellow
        $moduleName = Read-Host "Nome do módulo (ex: vk_inventory)"
        
        if (!$moduleName) {
            Write-Host "Nome é obrigatório!" -ForegroundColor Red
            exit 1
        }
        
        $modulePath = "addons\custom\$moduleName"
        
        if (Test-Path $modulePath) {
            Write-Host "Módulo já existe!" -ForegroundColor Red
            exit 1
        }
        
        # Criar estrutura básica
        New-Item -ItemType Directory -Path "$modulePath" -Force | Out-Null
        New-Item -ItemType Directory -Path "$modulePath\models" -Force | Out-Null
        New-Item -ItemType Directory -Path "$modulePath\views" -Force | Out-Null
        New-Item -ItemType Directory -Path "$modulePath\security" -Force | Out-Null
        
        # Criar __manifest__.py
        $manifest = @"
{
    "name": "$moduleName",
    "version": "18.0.1.0.0",
    "author": "VK Commodities",
    "category": "Custom",
    "summary": "Modulo customizado VK Commodities",
    "description": "Descricao do modulo $moduleName",
    "depends": ["base"],
    "data": [
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
}
"@
        $manifest | Out-File -FilePath "$modulePath\__manifest__.py" -Encoding UTF8
        
        # Criar __init__.py
        "# from . import models" | Out-File -FilePath "$modulePath\__init__.py" -Encoding UTF8
        "# from . import models" | Out-File -FilePath "$modulePath\models\__init__.py" -Encoding UTF8
        
        Write-Host "✅ Módulo $moduleName criado em: $modulePath" -ForegroundColor Green
        Write-Host "📝 Edite o __manifest__.py e adicione seus models/views" -ForegroundColor Cyan
    }
    
    "status" {
        Write-Host "STATUS DOS MÓDULOS:" -ForegroundColor Yellow
        Write-Host ""
        
        Write-Host "📁 MÓDULOS CUSTOMIZADOS (versionados):" -ForegroundColor Cyan
        $customModules = Get-ChildItem "addons\custom" -Directory -ErrorAction SilentlyContinue
        if ($customModules) {
            foreach ($module in $customModules) {
                Write-Host "  ✅ $($module.Name)" -ForegroundColor Green
            }
        } else {
            Write-Host "  ❌ Nenhum módulo customizado encontrado" -ForegroundColor Red
        }
        
        Write-Host ""
        Write-Host "📁 MÓDULOS OCA (versionados):" -ForegroundColor Cyan  
        $ocaModules = Get-ChildItem "addons\oca" -Directory -ErrorAction SilentlyContinue
        if ($ocaModules) {
            foreach ($module in $ocaModules) {
                Write-Host "  ✅ $($module.Name)" -ForegroundColor Green
            }
        } else {
            Write-Host "  ❌ Nenhum módulo OCA encontrado" -ForegroundColor Red
        }
    }
    
    default {
        Write-Host "Ação inválida: $Action" -ForegroundColor Red
        Write-Host "Use: .\scripts\manage-modules.ps1 help" -ForegroundColor Yellow
    }
}
