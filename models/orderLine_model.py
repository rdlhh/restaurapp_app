from odoo import models, fields, api

class orderLine(models.Model):
    _name = 'restaurapp_app.ol_model'
    _description = 'This is the order line model'

    order_id = fields.One2many("restaurapp_app.order_model", inverse_name="orderLine", string="Order", required=True)
    product_id = fields.Many2one("restaurapp_app.product_model", string="Product")
    quantity = fields.Char(string="Quantity Product", help="Quantity products of the table", required = True, default=-1)
    description = fields.Html(string="Description product", help="Description of the products")
