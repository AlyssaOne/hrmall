# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class Users(models.Model):
    _inherit = 'res.users'

    user_type = fields.Selection([(0, '管理员'), (1, 'Hr'), (2, '公司')], string='UserType', default=1)
    tel = fields.Char('Tel')
    gender = fields.Selection([('m', 'Man'), ('w', 'Woman')], 'Gender')
    register_time = fields.Datetime('RegisterTime')
    birth = fields.Date('Birthday')
    addr = fields.Text('Address')
    image = fields.Binary('HrImg')
    balance = fields.Float('Balance', default='0.0')
    my_company = fields.Many2one('hrmall.company', string='Company')
