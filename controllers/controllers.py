# -*- coding: utf-8 -*-
from odoo import http

# class Drplant(http.Controller):
#     @http.route('/drplant/drplant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drplant/drplant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('drplant.listing', {
#             'root': '/drplant/drplant',
#             'objects': http.request.env['drplant.drplant'].search([]),
#         })

#     @http.route('/drplant/drplant/objects/<model("drplant.drplant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drplant.object', {
#             'object': obj
#         })