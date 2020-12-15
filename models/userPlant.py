# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class UserPlant(models.Model):
    _name = 'drplant.userplant'
    
    date_watering = fields.Date()
    
    id_user = fields.Many2one('drplant.user')
    id_plant = fields.Many2one('drplant.plant')
    