# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# Ruben

from odoo import api
from odoo import fields
from odoo import models

class User(models.Model):
    _inherit = 'res.users'
    
    status = fields.Selection([('ENABLE', 'ENABLE'), ('DISABLE', 'DISABLE')], default='DISABLE')
    privilage = fields.Selection([('USER', 'USER'), ('ADMIN', 'ADMIN')], default='USER')
    lastAccess = fields.Date()
    lastPasswordChange = fields.Date()
    
    id_equipment = fields.Many2many('drplant.equipment')
    id_userplant = fields.One2many('drplant.userplant','id_user')
