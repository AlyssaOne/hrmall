# -*- coding: utf-8 -*-
from odoo import http

# class HrMall(http.Controller):
#     @http.route('/hr_mall/hr_mall/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_mall/hr_mall/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_mall.listing', {
#             'root': '/hr_mall/hr_mall',
#             'objects': http.request.env['hr_mall.hr_mall'].search([]),
#         })

#     @http.route('/hr_mall/hr_mall/objects/<model("hr_mall.hr_mall"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_mall.object', {
#             'object': obj
#         })