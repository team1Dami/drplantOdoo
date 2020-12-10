# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class UserPlant(models.Model):
    __name='drplant.UserPlant'
    
    date_watering=fields.Date()
    
    id_user=fields.Many2One(drplant.user)
    id_plant=fields.Many2One(drplant.plant)
    