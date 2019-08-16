# -*- coding: utf-8 -*-


from odoo import http


class HrRegister(http.Controller):
    @http.route('/hello', auth='public', type="http", website=True)
    def index(self, **kw):
        return ('hello')







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