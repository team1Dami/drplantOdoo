# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models
class Plant(models.Model):
    _name = 'drplant.plant'
    
    science_name = fields.Text(required=true)
    common_name = fields.Text()
    description = fields.Text()
    watering_frequence = fields.Timestamp()
    cares = fields.Text()
    climate = fields.Text()
    petfriendly = fields.Text()
    image = fields.binary()