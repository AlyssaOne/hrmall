# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrmallComment(models.Model):
    _name = 'hrmall.comment'

    user_name = fields.Many2one('hrmall.user', string='UserName', required=True)
    order_name = fields.Many2one('hrmall.order', string='OrderName', required=True)

    title = fields.Char('Title')
    content = fields.Text('Content')
    comment_time = fields.Datetime('CommentTime')
