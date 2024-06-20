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


    def _prepare_jump_to_sale_order(self, company_id):
        action = self.env["ir.actions.actions"]._for_xml_id(
            "sale.action_orders"
        )
        action = {
                "name": "Sale Order",
                "type": "ir.actions.act_window",
                "res_model": "sale.order",
                "view_type": "form",
                "view_mode": "form",
                "res_id": self.sale_id.id,
                "target": "current",
            }
        return action

    def jump_to_sale_order(self):
        self.ensure_one()
        company_id = self.company_id.id or self.env.company.id
        action = self._prepare_jump_to_sale_order(company_id)
        return action
