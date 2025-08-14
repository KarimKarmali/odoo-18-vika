@echo off
title Restart Odoo 18 VIKA
color 0E
echo ===============================================
echo          RESTART ODOO 18 VIKA
echo ===============================================
echo.
echo [INFO] Parando qualquer instancia existente do Odoo...

REM Parar processo Odoo existente
taskkill /F /IM python.exe >nul 2>&1
timeout /t 2 >nul

echo [OK] Processos parados
echo.
echo [INFO] Reiniciando servidor com atualizações...
echo.

REM Executar script principal
call iniciar_vika_18.bat

pause
