# -*- coding: utf-8 -*-
import os
from odoo import http
from odoo.http import request

class ManualContabilidade(http.Controller):
    
    @http.route('/manual_contabilidade', type='http', auth='user', website=True)
    def manual_contabilidade_page(self, **kwargs):
        """Servir o manual de contabilidade em HTML"""
        
        # Caminho para o arquivo HTML do manual
        module_path = os.path.dirname(os.path.dirname(__file__))  # account_usability directory
        manual_path = os.path.join(module_path, 'static', 'description', 'manual_contabilidade.html')
        
        try:
            with open(manual_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Retornar o HTML diretamente
            return html_content
            
        except Exception as e:
            error_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Erro - Manual de Contabilidade</title>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    .error {{ background: #f8d7da; color: #721c24; padding: 20px; border-radius: 5px; }}
                </style>
            </head>
            <body>
                <div class="error">
                    <h2>❌ Erro ao carregar o manual</h2>
                    <p><strong>Erro:</strong> {e}</p>
                    <p><strong>Caminho:</strong> {manual_path}</p>
                    <p>Verifique se o arquivo existe no diretório correto.</p>
                </div>
            </body>
            </html>
            """
            return error_html
