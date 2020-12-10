# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models
class Plant(models.Model):
    _name = 'drplant.plant'
    
    science_name = fields.Text(required=true,string="Science name")
    common_name = fields.Text(string="Science name")
    description = fields.Text()
    cares = fields.Text()
    watering_frequence = fields.Timestamp()
    petfriendly = fields.Selection([("cat", "cat" ),("dog","dog"),("both","both"),("no","no")])
    plant_type = fields.Selection([("indoor","indoor"),("outdoor","outdoor"),("succulent","succulent")])
    climate = fields.Selection([("hot","hot"),("cold","cold"),("dry","dry"),("wet","wet")]) 
    image = fields.image()
    
    id_shop=fields.Many2Many(drplant.shop)
    id_plague=fields.Many2Many(drplant.plague)
    id_userplant=fields.One2Many(drplant.userplant, id_plant)