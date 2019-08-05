# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('标题', required=True)
    date_release = fields.Date('出版日期')
    author_ids = fields.Many2many('res.partner', string='作者')
