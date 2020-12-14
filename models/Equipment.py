# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models
class Equipment (models.Model):
    _name = 'drplant.equipment'
    
    id_equipment = fields.Integer(requiered=True)
    equipment_description = fields.Text()
    equipment_name = fields.Text()
    image = field.Binary()
    price = field.Float()
    uses = field.Selection([('riego', 'riego'), ('sustrato', 'sustrato'), ('general', 'general'), ], 'Type', default='general')   

    shop = fields.Many2one('drplant.shop', onDelete="set null")
    user = fields.Many2many('drplant.user', string="user")