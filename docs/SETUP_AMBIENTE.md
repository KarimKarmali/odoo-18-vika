# Setup do Ambiente de Desenvolvimento - Odoo 18

## 📋 Pré-requisitos

Para desenvolver com Odoo 18, você precisa instalar:

### 1. Docker Desktop (RECOMENDADO)
- **Download**: https://www.docker.com/products/docker-desktop/
- **Vantagens**: Ambiente isolado, fácil configuração, produção-ready
- **Instalação**: Seguir instruções do site oficial

### 2. Alternativa: Python + PostgreSQL
- **Python 3.10+**: https://www.python.org/downloads/
- **PostgreSQL 15+**: https://www.postgresql.org/download/
- **Git**: https://git-scm.com/downloads
- **Node.js** (opcional para addons JS): https://nodejs.org/

## 🚀 Opção A: Desenvolvimento com Docker (RECOMENDADO)

### 1. Verificar Docker
```powershell
docker --version
docker-compose --version
```

### 2. Iniciar ambiente
```powershell
# Clone o projeto (se ainda não fez)
git clone https://github.com/KarimKarmali/odoo-18-vika.git
cd odoo-18-vika

# Executar
./scripts/run.ps1
```

### 3. Acessar Odoo
- URL: http://localhost:8069
- Master Password: admin123
- Criar nova database: nome qualquer (ex: vk_dev)

## 🐍 Opção B: Desenvolvimento com Python

### 1. Instalar dependências
```powershell
# Criar ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

# Instalar Odoo 18
pip install odoo==18.0

# Instalar dependências extras
pip install -r requirements.txt
```

### 2. Configurar PostgreSQL
```sql
-- Conectar ao PostgreSQL como admin
CREATE USER odoo WITH PASSWORD 'odoo';
CREATE DATABASE odoo_dev OWNER odoo;
ALTER USER odoo CREATEDB;
```

### 3. Configurar Odoo para Python
```powershell
# Copiar config para desenvolvimento Python
cp config/odoo.conf config/odoo-python.conf
```

### 4. Ajustar configuração
Editar `config/odoo-python.conf`:
```ini
[options]
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
addons_path = ./addons/custom,./addons/oca,C:\Path\To\Odoo\addons
```

### 5. Executar Odoo
```powershell
.\venv\Scripts\Activate.ps1
odoo -c config/odoo-python.conf --dev=all
```

## 🛠️ Desenvolvimento

### Estrutura do Projeto
```
odoo-18-vika/
├── addons/custom/      ← SEUS ADDONS
├── addons/oca/         ← ADDONS OCA
├── config/             ← CONFIGURAÇÕES
└── scripts/            ← SCRIPTS ÚTEIS
```

### Criar Novo Addon
1. Criar pasta: `addons/custom/meu_addon/`
2. Criar `__manifest__.py`
3. Desenvolver módulo
4. Testar: `scripts/test.sh meu_addon`

## 🔧 Troubleshooting

### Docker não funciona
- Instalar Docker Desktop
- Verificar se está rodando
- Verificar Hyper-V (Windows Pro)

### Python não funciona
- Instalar Python 3.10+
- Adicionar ao PATH
- Usar `py` em vez de `python`

### PostgreSQL
- Verificar se serviço está rodando
- Confirmar credenciais
- Testar conexão

## 📞 Suporte

- GitHub Issues: https://github.com/KarimKarmali/odoo-18-vika/issues
- Documentação Odoo: https://www.odoo.com/documentation/18.0/
