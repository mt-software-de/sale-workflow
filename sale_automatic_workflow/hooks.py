from odoo import api, SUPERUSER_ID
from odoo.tools.sql import column_exists, create_column


def pre_init_hook(cr):
    table = "sale_order"
    column = "all_qty_delivered"

    if not column_exists(cr, table, column):
        create_column(cr, table, column, "bool")

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['sale.order'].search([('state', '=', 'sale')])._compute_all_qty_delivered()
