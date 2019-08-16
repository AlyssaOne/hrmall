# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrmallFavorite(models.Model):
    _name = 'hrmall.favorite'

    user_name = fields.Many2one('hrmall.user', string='UserName', required=True)
    product_name = fields.Many2one('hrmall.product', string='ProductName', required=True)
