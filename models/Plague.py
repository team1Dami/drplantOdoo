# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import fields
from odoo import models

class Plague(models.Model):
    _name = 'drplant.plague'
    
    science_name = fields.Char(required=True) 
    common_name = fields.Char()
    description = fields.Text()
    remedy = fields.Text()
    control = fields.Text()
    plague_type = fields.Selection([('light', 'light'), ('midle', 'midle'), ('severe', 'severe')],default='midle')
    image = fields.Binary()
    
    id_plants = fields.Many2many('drplant.plant')