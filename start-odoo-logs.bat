@echo off
REM Script para Odoo 18 com logs salvos em arquivo
REM VK Commodities

title Odoo 18 com Logs - VK Commodities

REM Criar diretorio de logs se nao existir
if not exist "logs" mkdir logs

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

echo ========================================
echo  ODOO 18 - LOGS ATIVADOS
echo ========================================
echo URL: http://localhost:8069
echo Master Password: admin123  
echo Database: vk_dev
echo.
echo Logs salvos em: logs\odoo-debug.log
echo Para ver logs: tail -f logs\odoo-debug.log
echo ========================================

REM Executar Odoo com logs em arquivo
python odoo-source\odoo-bin ^
    -c config\odoo-python.conf ^
    -d vk_dev ^
    --dev=all ^
    --log-level=debug ^
    --logfile=logs\odoo-debug.log ^
    --log-handler=odoo.http:DEBUG ^
    --log-handler=odoo.sql_db:INFO ^
    --log-handler=odoo.modules:DEBUG

pause
