# -*- coding: utf-8 -*-
# from odoo import http


# class Wenk(http.Controller):
#     @http.route('/wenk/wenk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wenk/wenk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wenk.listing', {
#             'root': '/wenk/wenk',
#             'objects': http.request.env['wenk.wenk'].search([]),
#         })

#     @http.route('/wenk/wenk/objects/<model("wenk.wenk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wenk.object', {
#             'object': obj
#         })
