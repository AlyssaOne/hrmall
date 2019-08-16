# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrmallProduct(models.Model):
    _name = 'hrmall.product'

    product_name = fields.Char('ProductName', required=True)
    company_name = fields.Many2one('hrmall.company', string='CompanyName')

    detail = fields.Text('Detail', required=True)
    image = fields.Binary('Image', required=True)
    price = fields.Float('Price', default='1.0')
    status = fields.Selection([(0,'未上架'),(1,'已上架'),(2,'下架')],'Status', default=0)
    stock = fields.Integer('Stock', required=True)
    attribute = fields.Char('Attribute')
