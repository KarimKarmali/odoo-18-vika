/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Dialog } from "@web/core/dialog/dialog";
import { Component, xml } from "@odoo/owl";

class ManualModal extends Component {
    static template = xml`
        <Dialog title="'📖 Manual de Contabilidade VIKA'" size="'xl'" onClose="props.close">
            <div class="manual-container">
                <iframe 
                    src="/manual_contabilidade" 
                    style="width: 100%; height: 80vh; border: none; border-radius: 8px;"
                    onload="this.style.opacity = '1'"
                    style="opacity: 0; transition: opacity 0.3s;">
                </iframe>
            </div>
        </Dialog>
    `;
    static components = { Dialog };
}

// Função para abrir o modal
function openManualModal(env) {
    env.services.dialog.add(ManualModal, {
        close: () => {},
    });
}

// Registrar a ação
registry.category("actions").add("open_manual_modal", openManualModal);

// Função global para ser chamada pelo menu
window.openManualModal = function() {
    const env = odoo.__WOWL_DEBUG__.root.env;
    openManualModal(env);
};
