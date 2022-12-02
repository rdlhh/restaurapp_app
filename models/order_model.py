from odoo import models, fields, api

class order(models.Model):
    _name = 'restaurapp_app.order_model'
    _description = 'This is the order model'

    table = fields.Char(string="Table number", help="The number of the table", required=True, index=True)
    clients = fields.Char(string="Clients reference", help="The reference of clients")
    waiter = fields.Char(string="Waiter", help="The name of the waiter", required=True)
    pax = fields.Char(string="Clients number", help="The number of the clients", required=True)
    productOrder = fields.One2many("restaurapp_app.product_model", inverse_name="order", string="Product", required=True)
    tPrice = fields.Float(string="Price", help="The total price of the order")
    orderLine = fields.Many2one("restaurapp_app.ol_model", string="OrderLine")
