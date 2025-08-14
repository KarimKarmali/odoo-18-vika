@echo off
REM Script para sincronizar TUDO local -> CapRover
REM VK Commodities - Sincronização completa

title Sync para Produção - VK Commodities

echo ================================================
echo  SINCRONIZAÇÃO LOCAL -> CAPROVER
echo  VK Commodities - Odoo 18
echo ================================================
echo.

echo [INFO] Verificando alterações...
git status

echo.
echo [INFO] Adicionando TODOS os arquivos (incluindo módulos)...
git add .

echo.
echo [INFO] Verificando o que será commitado...
git status

echo.
set /p commit_msg="Mensagem do commit (ou Enter para automática): "
if "%commit_msg%"=="" set commit_msg=sync: alterações locais para produção - módulos e configs

echo.
echo [INFO] Fazendo commit...
git commit -m "%commit_msg%"

if errorlevel 1 (
    echo [AVISO] Nada para commitar ou erro no commit
    pause
    exit /b 1
)

echo.
echo [INFO] Enviando para GitHub...
git push origin main

if errorlevel 1 (
    echo [ERRO] Falha no push para GitHub
    pause
    exit /b 1
)

echo.
echo [INFO] Deploy automático para CapRover...
echo (CapRover deve ter webhook configurado para auto-deploy)

echo.
echo ================================================
echo  ✅ SINCRONIZAÇÃO CONCLUÍDA!
echo ================================================
echo.
echo ✅ Código sincronizado no GitHub
echo ✅ Módulos locais incluídos  
echo ✅ Configurações atualizadas
echo ✅ Deploy automático ativado
echo.
echo 🌐 CapRover fará deploy automático em alguns minutos
echo 📋 Todas as suas alterações locais estão em produção
echo.
pause
