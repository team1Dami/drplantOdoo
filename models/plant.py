# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# Ruben

from odoo import api
from odoo import fields
from odoo import models
import re 
from odoo.exceptions import ValidationError

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
    
    id_shop = fields.Many2many('drplant.shop', string="Tiendas", ondelete="null")
    id_plague = fields.Many2many('drplant.plague', string="Plagas", ondelete="null")
    id_userplant = fields.One2many('drplant.userplant', 'id_plant')
    
    
    @api.constrains('watering_frequence')
    def _check_watering_frequence_not_null(self):
        for Plant in self:
            if Plant.watering_frequence < 0:
                raise ValidationError("You can`t enter a negative number: %s" % Plant.watering_frequence)
            
    @api.onchange('common_name')
    def _check_common_name_do_not_start_with_number(self):
        if self.common_name:
            match = re.match(r'^[a-zA-Z][ a-zA-Z]*', self.common_name)
            if match == None:
                raise ValidationError('Cannot start with number')