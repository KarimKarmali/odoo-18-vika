@echo off
REM Script para iniciar Odoo 18 - VK Commodities
REM Com logs completos e ambiente virtual ativado

title Odoo 18 - VK Commodities

echo ========================================
echo  ODOO 18 - VK COMMODITIES 
echo ========================================
echo.

REM Verificar se ambiente virtual existe
if not exist "venv\Scripts\activate.bat" (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo Execute primeiro: scripts\install-requirements.ps1
    pause
    exit /b 1
)

echo [INFO] Ativando ambiente virtual...
call venv\Scripts\activate.bat

echo [INFO] Verificando Python...
python --version
if errorlevel 1 (
    echo [ERRO] Python nao encontrado no ambiente virtual!
    pause
    exit /b 1
)

echo [INFO] Verificando PostgreSQL...
netstat -an | find ":5432" > nul
if errorlevel 1 (
    echo [AVISO] PostgreSQL pode nao estar rodando na porta 5432
    echo Continue mesmo assim? (S/N)
    set /p continue=
    if /i not "%continue%"=="S" exit /b 1
)

echo.
echo ========================================
echo  INICIANDO ODOO 18
echo ========================================
echo URL: http://localhost:8069
echo Master Password: admin123
echo Database: vk_dev
echo.
echo Pressione Ctrl+C para parar
echo ========================================
echo.

REM Executar Odoo com logs detalhados
python odoo-source\odoo-bin ^
    -c config\odoo-python.conf ^
    -d vk_dev ^
    --dev=all ^
    --log-level=debug ^
    --log-handler=odoo.http:DEBUG ^
    --log-handler=odoo.sql_db:INFO

echo.
echo [INFO] Odoo parado.
pause
