# -*- coding: utf-8 -*-
# from odoo import http


# class Instalacion(http.Controller):
#     @http.route('/instalacion/instalacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instalacion/instalacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('instalacion.listing', {
#             'root': '/instalacion/instalacion',
#             'objects': http.request.env['instalacion.instalacion'].search([]),
#         })

#     @http.route('/instalacion/instalacion/objects/<model("instalacion.instalacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instalacion.object', {
#             'object': obj
#         })
