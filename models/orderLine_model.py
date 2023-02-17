from odoo import models, fields, api

class orderLine(models.Model):
    _name = 'restaurapp_app.ol_model'
    _description = 'This is the order line model'

    order_id = fields.Many2one("restaurapp_app.order_model")
    product_id = fields.Many2one("restaurapp_app.product_model", string="Product", required=True)
    quantity = fields.Integer(string="Quantity Product", help="Quantity products of the table", required = True, default=1)
    description = fields.Text(string="Description product", help="Description of the products")
    state = fields.Selection([ ('P','Preparation'),('D','Done'),('DV','Delivered'),],string='state',default='P')


    def changeStateDone(self):    
        self.state = 'D'
        self.order_id.changeColor()

    def changeStateDelivered(self):    
        self.state = 'DV'
        self.order_id.changeColor()