from odoo import models, fields, api

class orderLine(models.Model):
    _name = 'restaurapp_app.ol_model'
    _description = 'This is the order line model'

    order_id = fields.Many2one("restaurapp_app.order_model")
    product_id = fields.Many2one("restaurapp_app.product_model", string="Product", required=True)
    quantity = fields.Integer(string="Quantity Product", help="Quantity products of the table", required = True, default=1)
    description = fields.Html(string="Description product", help="Description of the products")
    isdone = fields.Boolean(string="Is done?", help="The line is done?")
    active = fields.Boolean(string="Is the order active?", help="The order is active?", default=True)


    @api.onchange("isdone")
    def changeActiveTask(self):
        self.active = not self.isdone
        self.isdone = not self.active
        if self.isdone:
            self.active = False

    def changeLine(self):
        self.ensure_one()
        self.isdone = not self.isdone
        self.active = not self.isdone