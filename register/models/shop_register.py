# -*- coding: utf-8 -*-

from odoo import models, fields, api

class shopregister(models.Model):
     _name = 'shop.register'

     name = fields.Char(string=u'用户名', required=True)
     password = fields.Char(string=u'密码', required=True)
     email = fields.Char(string=u'邮箱', required=True)