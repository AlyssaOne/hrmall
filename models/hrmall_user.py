from odoo import models, fields, api

class HrmallUser(models.Model):
    _name = 'hrmall.user'

    user_name = fields.Char(string='UserName')

    pwd = fields.Char('Pwd', required=True)
    user_type = fields.Selection([(0,'管理员'),(1,'Hr'),(2,'公司')],string='UserType', default=1)
    status = fields.Selection([(0,'待审核'),(1,'已通过')],'Status',default=0)


