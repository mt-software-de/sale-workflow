from odoo import api, models, fields, _


class Route(models.Model):
    _inherit = "stock.location.route"

    no_sale_stock_prebook = fields.Boolean(
        string="No Prebook Stock",
        help="Prevents stock from prebooking when set."
             "\nIf not set stock prebooks itself automatically.",
    )
