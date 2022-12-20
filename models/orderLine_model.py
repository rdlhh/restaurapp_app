from odoo import models, fields, api

class orderLine(models.Model):
    _name = 'restaurapp_app.ol_model'
    _description = 'This is the order line model'

    order_id = fields.Many2one("restaurapp_app.order_model", string="Order")
    product_id = fields.Many2one("restaurapp_app.product_model", string="Product")
    quantity = fields.Integer(string="Quantity Product", help="Quantity products of the table", required = True)
    description = fields.Html(string="Description product", help="Description of the products")
