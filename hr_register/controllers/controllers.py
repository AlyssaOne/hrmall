# -*- coding: utf-8 -*-
from odoo import http

# class HrRegister(http.Controller):
#     @http.route('/hr_register/hr_register/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_register/hr_register/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_register.listing', {
#             'root': '/hr_register/hr_register',
#             'objects': http.request.env['hr_register.hr_register'].search([]),
#         })

#     @http.route('/hr_register/hr_register/objects/<model("hr_register.hr_register"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_register.object', {
#             'object': obj
#         })