# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Plant(models.Model):
    _name = 'drplant.plant'
    
    science_name = fields.Char(required=True, string="Science name")
    common_name = fields.Char(string="Common name")
    description = fields.Text()
    cares = fields.Text()
    watering_frequence = fields.Float()
    petfriendly = fields.Selection([('cat', 'cat'), ('dog', 'dog'), ('both', 'both'), ('no', 'no')], default='cat')
    plant_type = fields.Selection([('indoor', 'indoor'), ('outdoor', 'outdoor'), ('succulent', 'succulent')], default='indoor')
    climate = fields.Selection([('hot', 'hot'), ('cold', 'cold'), ('dry', 'dry'), ('wet', 'wet')], default='dry') 
    image = fields.Binary()
    
    id_shop = fields.Many2many('drplant.shop', string="Tiendas")
    id_plague = fields.Many2many('drplant.plague', string="Plagas")
    id_userplant = fields.One2many('drplant.userplant', 'id_plant')