# -*- coding: utf-8 -*-
from openerp import http

# class Fortuna(http.Controller):
#     @http.route('/fortuna/fortuna/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fortuna/fortuna/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fortuna.listing', {
#             'root': '/fortuna/fortuna',
#             'objects': http.request.env['fortuna.fortuna'].search([]),
#         })

#     @http.route('/fortuna/fortuna/objects/<model("fortuna.fortuna"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fortuna.object', {
#             'object': obj
#         })