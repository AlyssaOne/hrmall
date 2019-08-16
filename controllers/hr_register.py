# -*- coding: utf-8 -*-

import datetime
from odoo import http
from ..models.hrmall_hr import  HrmallHr
from ..models.hrmall_user import HrmallUser
class HrRegister(http.Controller):
    @http.route('/user/register/', auth='public', type="http", website=True)
    def index(self, **kw):
        return http.request.render("hrmall.index")

    @http.route('/login', auth='public', type="http", website=True)
    def login(self, **kw):
        values = {}
        for field_name, field_value in kw.items():
            values[field_name] = field_value

        cur = datetime.datetime.now()
        http.request.env['hrmall.user'].sudo().create({'user_name':values['user_name'],'pwd':values['pwd'],'user_type':1,'status':0})
        username = http.request.env['hrmall.user'].search([('user_name','=',values['user_name'])])
        http.request.env['hrmall.hr'].sudo().create({'hr_name':values['hr_name'],'user_name':username.id,'card_num':values['card_num'],
                                                     'tel':values['tel'],'gender':values['gender'],'register_time':cur,'birth':values['birth'],
                                                     'email':values['email'],'addr':values['addr'],'image':values['image']})
        return http.request.render("hrmall.login")