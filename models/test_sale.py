from random import randint
from lxml import etree
import json
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class TestSale(models.Model):
    _inherit = "sale.order"

    test = fields.Char(string="Test", default=str(randint(100, 10000)))

    @api.onchange("tax_totals_json")
    def _onchange_line(self):
        total = json.loads(self.tax_totals_json)
        if (not (total['amount_total'] == 0)):
            self.test = f"{total['amount_total']} - {self.date_order}"
    
    @api.constrains("test")
    def check_test(self):

        if (self.test):    
            if (len(self.test) > 50):
                raise ValidationError("Длина текста должна быть меньше 50 символов!")