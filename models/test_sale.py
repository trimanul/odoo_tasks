from random import randint
from odoo import api, fields, models

class TestSale(models.Model):
    _inherit = "sale.order"

    test = fields.Char(string="Test", compute="_compute_random")
    @api.depends("test")
    def _compute_random(self):
            for record in self:
                record.test = randint(0, 100)