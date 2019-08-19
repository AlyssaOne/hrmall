from odoo import models, fields, api


class HrmallCompany(models.Model):
    _name = 'hrmall.company'
    _rec_name = 'company_name'

    company_name = fields.Char('CompanyName', required=True)
    # user_name = fields.Many2one('res.users', string='UserName')

    city = fields.Text('City')
    country = fields.Char('Country')
    tel = fields.Char('Tel')
    detail = fields.Text('Detail')
    zip = fields.Char('Zip')
    email = fields.Text('Email')
    adrr = fields.Text('Address')
    image = fields.Binary('CompanyLogo')
    balance = fields.Float('Balance', default='0.0')
