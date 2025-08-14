# Como Usar - Odoo 18 VK Commodities

## 🚀 Scripts Disponíveis

### 1. **start-odoo.bat** (Completo)
- Verifica ambiente virtual
- Verifica PostgreSQL 
- Inicia Odoo com logs detalhados
- Interface mais amigável

### 2. **dev.bat** (Rápido)
- Inicio rápido para desenvolvimento
- Sem verificações extras
- Ideal para uso diário

### 3. **start-odoo-logs.bat** (Com Arquivo de Logs)
- Salva logs em `logs/odoo-debug.log`
- Útil para debug e análise
- Logs persistem após fechar

## 📋 Uso Básico

### Primeira vez:
1. Execute: `scripts/install-requirements.ps1`
2. Duplo-click em: `start-odoo.bat`

### Desenvolvimento diário:
- Duplo-click em: `dev.bat`

## 🌐 Acesso

- **URL**: http://localhost:8069
- **Master Password**: `admin123`
- **Database**: `vk_dev`

## 🛠️ Desenvolvimento

### Criar novo addon:
1. Criar pasta: `addons/custom/meu_addon/`
2. Adicionar `__manifest__.py`
3. Reiniciar Odoo (Ctrl+C no .bat)

### Logs em tempo real:
```powershell
# Em outro terminal
Get-Content logs\odoo-debug.log -Wait
```

## ❌ Problemas Comuns

### "Python não encontrado"
- Execute `scripts/install-requirements.ps1` primeiro

### "PostgreSQL não conecta" 
- Verifique se PostgreSQL está rodando
- Porta 5432 deve estar aberta

### "Módulo não carrega"
- Reinicie Odoo
- Verifique `__manifest__.py`
- Confira logs para erros

## 📞 Suporte

- Logs detalhados em: `logs/odoo-debug.log`
- Configuração em: `config/odoo-python.conf`
