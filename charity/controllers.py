# -*- coding: utf-8 -*-
# from odoo import http


# class Charity(http.Controller):
#     @http.route('/charity/charity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/charity/charity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('charity.listing', {
#             'root': '/charity/charity',
#             'objects': http.request.env['charity.charity'].search([]),
#         })

#     @http.route('/charity/charity/objects/<model("charity.charity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('charity.object', {
#             'object': obj
#         })
