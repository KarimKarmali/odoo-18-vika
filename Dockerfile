# Dockerfile para Odoo 18 - VK Commodities
# Otimizado para desenvolvimento e produção CapRover

FROM odoo:18

USER root

# Instalar dependências adicionais se necessário
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar addons customizados
COPY addons/custom /opt/odoo/addons/custom
COPY addons/oca /opt/odoo/addons/oca

# Copiar configuração
COPY config/odoo.conf /etc/odoo/

# Configurar permissões
RUN chown -R odoo:odoo /opt/odoo/addons/custom /opt/odoo/addons/oca

USER odoo

# Expor porta
EXPOSE 8069

# Comando de entrada
CMD ["odoo", "-c", "/etc/odoo/odoo.conf"]
