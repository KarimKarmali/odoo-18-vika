@echo off
REM Script rapido para desenvolvimento Odoo 18

title Odoo 18 DEV - VK Commodities

call venv\Scripts\activate.bat

echo Iniciando Odoo 18 em modo desenvolvimento...
echo URL: http://localhost:8069

python odoo-source\odoo-bin -c config\odoo-python.conf -d vk_dev --dev=all

pause
