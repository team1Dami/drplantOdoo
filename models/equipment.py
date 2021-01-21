# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Equipment (models.Model):
    _name = 'drplant.equipment'
    
    equipment_description = fields.Text()
    equipment_name = fields.Text()
    image = fields.Binary()
    price = fields.Float()
    uses = fields.Selection([('riego', 'riego'), ('sustrato', 'sustrato'), ('general', 'general'), ], 'Type', default='general')   

    shop = fields.Many2one('drplant.shop', onDelete="set null")
    user = fields.Many2many('drplant.user', string="user")