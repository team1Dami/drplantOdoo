# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Shop(models.Model):
    _name = 'drplant.shop'
    
    shop_name = fields.Char()
    url = fields.Char()
    location = fields.Text()
    commission = fields.Float()
    email = fields.Text()

    equipment = fields.One2many('drplant.equipment', 'id', string="Equipments")
    plant = fields.Many2many('drplant.plant',string="Plants")