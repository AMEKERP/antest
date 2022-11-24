# -*- coding: utf-8 -*-
# from odoo import http


# class Recipient(http.Controller):
#     @http.route('/recipient/recipient/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recipient/recipient/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recipient.listing', {
#             'root': '/recipient/recipient',
#             'objects': http.request.env['recipient.recipient'].search([]),
#         })

#     @http.route('/recipient/recipient/objects/<model("recipient.recipient"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recipient.object', {
#             'object': obj
#         })
