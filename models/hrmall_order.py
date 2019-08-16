# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrmallOrder(models.Model):
    _name = 'hrmall.order'

    user_name = fields.Many2one('hrmall.user', string='UserName', required=True)
    product_name = fields.Many2one('hrmall.product', string='ProductName', required=True)
    company_name = fields.Many2one('hrmall.company', string='CompanyName')

    order_num = fields.Char('OrderNum', required=True)
    product_count = fields.Integer('ProductCount', required=True)
    payment = fields.Float('Payment', required=True)
    status = fields.Selection([(0,'已取消'),(1,'未付款'),(2,'已付款'),
                               (3,'已发货'),(4,'交易完成')],'Status', default=1)   #0:已取消，1:未付款，2:已付款；3:已发货；4:交易成功
    payment_time = fields.Datetime('PaymentTime')
    send_time = fields.Datetime('SendTime')
    create_time = fields.Datetime('CreateTime')
    end_time = fields.Datetime('EndTime')
    remark = fields.Text('Remark')
    file = fields.Binary('File')
