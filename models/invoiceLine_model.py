from odoo import models, fields, api

class InvoiceLine(models.Model):
    _name = 'restaurapp_app.il_model'
    _description = 'This is a line invoice model.'

    lineId = fields.Many2one("restaurapp_app.invoice_model")
    quantity = fields.Integer(string="Quantity",help="Quantity of the product.", default=1)
    product = fields.Many2one("restaurapp_app.product_model", string="Product", default=1)
    description = fields.Html(string="Description",help="Description of the product")