# Copyright 2024 Akretion France (http://www.akretion.com/)
# @author: Mathieu Delva <mathieu.delva@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    stock_is_reserved = fields.Boolean(
        "Stock is reserved",
        related="sale_id.stock_is_reserved"
    )

    def jump_to_sale_order(self):
        self.ensure_one()
        return self.sale_id.get_formview_action()
