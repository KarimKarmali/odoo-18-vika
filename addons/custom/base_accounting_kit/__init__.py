# -*- # -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from . import models
from . import report
from . import wizard


def post_init_hook(env):
    """Post installation hook to ensure accounting menus are visible"""
    # Force reload of all menu items for accounting
    menus_to_update = [
        'account.menu_finance',
        'account.menu_finance_reports', 
        'account.menu_finance_configuration',
        'account.menu_board_journal_1',
        'account.menu_action_move_out_invoice_type',
        'account.menu_action_move_in_invoice_type',
        'account.menu_finance_entries',
    ]
    
    for menu_xml_id in menus_to_update:
        try:
            menu = env.ref(menu_xml_id, raise_if_not_found=False)
            if menu:
                # Force update groups_id to ensure visibility
                invoice_group = env.ref('account.group_account_invoice', raise_if_not_found=False)
                if invoice_group:
                    menu.write({'groups_id': [(6, 0, [invoice_group.id])]})
        except Exception:
            # Ignore errors and continue
            pass
    
    # Clear menu cache
    env['ir.ui.menu'].clear_caches()
    env.registry._init_modules.add('base_accounting_kit')
