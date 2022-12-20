from odoo import models, fields, api

class order(models.Model):
    _name = 'restaurapp_app.order_model'
    _description = 'This is the order model'

    table = fields.Char(string="Table number", help="The number of the table", required=True, index=True)
    clients = fields.Char(string="Clients reference", help="The reference of clients")
    waiter = fields.Char(string="Waiter", help="The name of the waiter", required=True)
    pax = fields.Char(string="Clients number", help="The number of the clients", required=True)
    tPrice = fields.Float(string="Price", help="The total price of the order", compute="_getTotalPrice", store=True)
    orderLine = fields.One2many("restaurapp_app.ol_model", "quantity", string="Products", required=True)


    @api.depends("orderLine")
    def _getTotalPrice(self):
        self.tPrice = 0
        for line in self.orderLine:
            self.tPrice += line.quantity * line.product_id.price