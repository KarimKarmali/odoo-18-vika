# COMO CORRIGIR O ZIP DO MIS_BUILDER

## Problema
O ZIP baixado contém o arquivo original problemático do date_range.

## Solução
1. **Extrair o ZIP:**
   - Extrair `mis_builder-18.0.1.0.0.zip` para uma pasta temporária

2. **Localizar e corrigir:**
   - Navegar até `date_range/data/ir_cron_data.xml`
   - Substituir todo o conteúdo por:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<odoo noupdate="1">
    <!-- Cron job removido para evitar erro de referência circular -->
    <!-- Será criado automaticamente via código Python após instalação -->
</odoo>
```

3. **Recriar o ZIP:**
   - Comprimir novamente a pasta modificada
   - Fazer upload do novo ZIP

## Alternativa Rápida
- Usar os módulos locais já corrigidos em `addons/oca/`
- Não fazer upload via ZIP
