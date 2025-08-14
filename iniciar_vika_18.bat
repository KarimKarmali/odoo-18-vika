@echo off
title Odoo 18 VIKA
color 0A
echo ===============================================
echo            INICIANDO ODOO 18 VIKA
echo ===============================================
echo.

REM Definir variáveis
set "ODOO_ROOT=%~dp0"
set "PYTHON_PATH=C:\Users\karim\AppData\Local\Programs\Python\Python310\python.exe"

echo [INFO] Verificando ambiente...

REM Verificar se o Python existe
if not exist "%PYTHON_PATH%" (
    echo [ERRO] Python não encontrado em: %PYTHON_PATH%
    echo Verifique se o Python 3.10 está instalado.
    pause
    exit /b 1
)
echo [OK] Python encontrado: %PYTHON_PATH%

REM Navegar para o diretório do script (que é o raiz do Odoo)
echo [INFO] Diretório do projeto: %ODOO_ROOT%
cd /d "%ODOO_ROOT%"

REM Verificar se os arquivos necessários existem
if not exist "odoo-bin" (
    echo [ERRO] Arquivo odoo-bin não encontrado!
    echo Diretório atual: %CD%
    echo Verifique se está no diretório correto do Odoo.
    pause
    exit /b 1
)
echo [OK] odoo-bin encontrado

if not exist "odoo_vika_18.conf" (
    echo [ERRO] Arquivo de configuração odoo_vika_18.conf não encontrado!
    echo Diretório atual: %CD%
    echo Verifique se o arquivo de configuração existe.
    pause
    exit /b 1
)
echo [OK] odoo_vika_18.conf encontrado

if not exist "odoo" (
    echo [ERRO] Diretório odoo/ não encontrado!
    echo Diretório atual: %CD%
    echo Verifique se o código fonte do Odoo está presente.
    pause
    exit /b 1
)
echo [OK] Diretório odoo/ encontrado

echo.
echo ===============================================
echo [INFO] Iniciando servidor Odoo 18 VIKA...
echo [INFO] Diretório: %CD%
echo [INFO] Base de dados: vika_odoo18
echo [INFO] Porta: 8069
echo [INFO] Modo desenvolvedor: Ativado
echo ===============================================
echo.
echo Aguarde... O servidor pode demorar alguns minutos para iniciar.
echo Quando estiver pronto, acesse: http://localhost:8069
echo Para parar o servidor, pressione Ctrl+C
echo.

"%PYTHON_PATH%" odoo-bin -c odoo_vika_18.conf -d vika_odoo18 --dev=assets,reload --without-demo=all

echo.
echo ===============================================
echo   SERVIDOR PARADO - Prima qualquer tecla...
echo ===============================================
pause
