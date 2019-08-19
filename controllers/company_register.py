import datetime
from odoo import http
from ..models.res_users  import Users
from ..models.hrmall_company import HrmallCompany

class HrRegister(http.Controller):
    @http.route('/shop/register/', auth='public', type="http", website=True)
    def index(self, **kw):
        return http.request.render("hrmall.company")

    @http.route('/shop/login', auth='public', type="http", website=True)
    def login(self, **kw):
        values = {}
        for field_name, field_value in kw.items():
            values[field_name] = field_value

        cur = datetime.datetime.now()
        http.request.env['hrmall.company'].sudo().create({'company_name':values['company_name']})
        company = http.request.env['hrmall.company'].search([('company_name','=',values['company_name'])])
        http.request.env['res.partner'].sudo().create({'name':values['name'],'active':'false','email':values['email']})
        partner = http.request.env['res.partner'].search([('name','=',values['name'])])
        http.request.env['res.users'].sudo().create({'login':values['email'],'password':values['password'],'active':'false','user_type':2,'my_company':company.id,
                                                    'company_id':1,'partner_id':partner.id,'notification_type':'email','odoobot_state':'not_initialized'})
                                              #      'tel':values['tel'],'gender':values['gender'],'register_time':cur,'birth':values['birth'],
                                               #      'email':values['email'],'addr':values['addr']})
        return http.request.render("hrmall.login")