# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# Gonzalo

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class Shop(models.Model):
    _name = 'drplant.shop'
    
    shop_name = fields.Char()
    url = fields.Char()
    location = fields.Text()
    commission = fields.Float()
    email = fields.Text()

    equipment = fields.One2many('drplant.equipment', 'id', string="Equipments")
    plant = fields.Many2many('drplant.plant',string="Plants")
    
    @api.constrains('commission')
    def _check_commission(self):
        for Shop in self:
            if Shop.commission > 20:
                raise ValidationError("The commission is too high: %s" % Shop.commission)
