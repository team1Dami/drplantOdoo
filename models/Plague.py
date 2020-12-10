# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class Plague(models.Model):
    __name='new_module.Plague'
    science_name = fields.Char(required=True) 
    common_name = fields.Char()
    description = fields.Text()
    remedy = fields.Text()
    control = fields.Text()
    type = fields.Selection()
    image