# -*- coding: utf-8 -*-


from odoo import http

from ..models.models import hrregister
class HrRegister(http.Controller):
    @http.route('/user/register/', auth='public', type="http", website=True)
    def index(self, **kw):
        return http.request.render("hrmall.index")

    @http.route('/login', auth='public', type="http", website=True)
    def login(self, **kw):
        values = {}
        for field_name, field_value in kw.items():
            values[field_name] = field_value
        http.request.env['hrmall.hrregister'].sudo().create({'name':values['name'],'email':values['email'],'password':values['password']})
        return http.request.render("hrmall.login")





#     @http.route('/register/register/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('register.listing', {
#             'root': '/register/register',
#             'objects': http.request.env['register.register'].search([]),
#         })

#     @http.route('/register/register/objects/<model("register.register"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('register.object', {
#             'object': obj
#         })