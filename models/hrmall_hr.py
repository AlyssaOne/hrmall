from odoo import models, fields, api

class HrmallHr(models.Model):
    _name = 'hrmall.hr'

    hr_name = fields.Char('HrName')
    user_name = fields.Many2one('hrmall.user', string='UserName')

    card_num = fields.Text('CardNumber')
    tel = fields.Char('Tel')
    gender = fields.Selection([('m','Man'),('w','Woman')],'Gender')
    register_time = fields.Datetime('RegisterTime')
    birth = fields.Datetime('Birthday')
    email = fields.Text('Email')
    addr = fields.Text('Address')
    image = fields.Binary('HrImg')
    balance = fields.Float('Balance', default='0.0')
