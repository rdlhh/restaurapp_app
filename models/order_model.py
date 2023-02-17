import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class order(models.Model):
    _name = 'restaurapp_app.order_model'
    _description = 'This is the order model'
    _rec_name = "table"

    table = fields.Char(string="Table number", help="The number of the table", required=True, index=True)
    clients = fields.Text(string="Client name", help="The reference of clients", required=True)
    waiter = fields.Char(string="Waiter", help="The name of the waiter", required=True, default=lambda self:self.env.user.name)
    pax = fields.Char(string="Clients number", help="The number of the clients", default=1)
    tPrice = fields.Float(string="Price", help="The total price of the order", compute="_getTotalPrice", store=True)
    orderLine = fields.One2many("restaurapp_app.ol_model", "order_id", string="Products", required=True)
    state = fields.Selection(string="State: ", selection=[('A', 'Active'), ('C', 'Confirmed')], default="A")
    stateLine = fields.Selection([ ('W','Wait'),('D','Delivered'),('F','Finish'),],string='Action: ',default="W")


    @api.depends("orderLine")
    def _getTotalPrice(self):
        self.tPrice = 0
        for line in self.orderLine:
            self.tPrice += line.quantity * line.product_id.price

        self.changeColor()

    @api.depends("orderLine")
    def changeColor(self):
        flagD = False
        flagW = False
         
        for line in self.orderLine:
            if line.state == "P":
                flagW = True
            elif line.state == "D":
                flagD = True
            
        if flagD == True:
            self.stateLine = "D"
        elif flagW == True:
            self.stateLine = "W"
        else:
            self.stateLine = "F"


    def confirmOrder(self):
        for l in self.orderLine:
            if l.state != 'DV':
                raise ValidationError("The order is not finished!")
        self.state = 'C'
        invoice = {}
        invoice["client"] = self.clients
        invoice["base"] = self.tPrice
        inv = self.env['restaurapp_app.invoice_model'].sudo().create(invoice)
        for ol in self.orderLine:
            line = {}
            line["lineId"] = inv.id
            line["quantity"] = ol.quantity
            line["product"] = ol.product_id.id
            line["description"] = ol.description
            self.env["restaurapp_app.il_model"].sudo().create(line)

    @api.onchange("table")
    def changeNameClients(self):
        self.clients = "Mesa "+ str(self.table)

        
            
