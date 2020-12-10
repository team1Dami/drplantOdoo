# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Shop(models.Model):
    __name='new_module.shop'
    id_shop = fields.Integer(required = True)
    shop_name = fields.Char()
    url = fields.Char()
    locatiom = fields.String()
    commission = fields.Float()
    email = fields.String()
