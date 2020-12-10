# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields,api

class User(models.Model):
    __name='new_module.User'
    
    user_id = fields.Integer(required==True)
    login = fields.Char(required=True)
    fullName = fields.Char()
    password = fields.Char()
    email = fields.Char()
    status = fields.Selection()
    privilage = fields.Selection()
    lastAccess = fields.Date()
    lastPasswordChange = fields.Date()
    
    
