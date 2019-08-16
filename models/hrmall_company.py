from odoo import models, fields, api

class HrmallCompany(models.Model):
    _name = 'hrmall.company'

    company_name = fields.Char('CompanyName', required=True)
    user_name = fields.Many2one('hrmall.user',string='UserName')

    city = fields.Text('City')
    country = fields.Char('Country')
    tel = fields.Char('Tel')
    detail = fields.Text('Detail')
    zip = fields.Char('Zip')
    email = fields.Text('Email')
    adrr = fields.Text('Adrress')
    image = fields.Binary('CompanyLogo')
    balance = fields.Float('Balance',default='0.0')

