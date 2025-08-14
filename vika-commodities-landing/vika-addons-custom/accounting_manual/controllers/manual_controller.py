# -*- coding: utf-8 -*-
import os
from odoo import http
from odoo.http import request

# Fallback simples se markdown não estiver disponível
try:
    import markdown
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False


class AccountingManual(http.Controller):
    
    @http.route('/accounting_manual', type='http', auth='user', website=True)
    def accounting_manual(self, **kwargs):
        """Controlador para exibir o manual de contabilidade"""
        
        # Caminho para o arquivo markdown
        module_path = os.path.dirname(os.path.dirname(__file__))
        manual_path = os.path.join(module_path, 'static', 'description', 'ACCOUNTING_MANUAL.md')
        
        # Ler o conteúdo do markdown
        try:
            with open(manual_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # Converter markdown para HTML se disponível
            if HAS_MARKDOWN:
                html_content = markdown.markdown(
                    markdown_content, 
                    extensions=['extra', 'codehilite', 'toc']
                )
            else:
                # Conversão simples sem markdown
                html_content = markdown_content.replace('\n', '<br>')
            
        except Exception as e:
            html_content = f"""
            <div class="alert alert-danger">
                <h4>Erro ao carregar o manual</h4>
                <p>Não foi possível carregar o conteúdo do manual de contabilidade.</p>
                <p><strong>Erro:</strong> {str(e)}</p>
            </div>
            """
        
        # Preparar dados para o template
        values = {
            'manual_content': html_content,
            'page_title': 'Manual de Contabilidade VIKA',
        }
        
        # Renderizar template
        return request.render('accounting_manual.accounting_manual_page', values)
    
    @http.route('/accounting_manual/api/content', type='json', auth='user')
    def get_manual_content(self, **kwargs):
        """API endpoint para carregar conteúdo via AJAX"""
        
        module_path = os.path.dirname(os.path.dirname(__file__))
        manual_path = os.path.join(module_path, 'static', 'description', 'ACCOUNTING_MANUAL.md')
        
        try:
            with open(manual_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                'status': 'success',
                'content': content,
                'html': markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
