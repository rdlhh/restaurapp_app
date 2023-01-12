from datetime import datetime
from odoo import models, fields, api


class product(models.Model):
  _name = 'invoice.invoice_model'
  _description = 'This is the invoice model'

  ref = fields.Integer(string="Invoice reference", help="Number of the invoice", required=True, index=True)
  date = fields.Datetime(string="Date", help="Description of the invoice", required=True, default=lambda self:datetime.now())
  currency_id = fields.Many2one('res.currency', string="Currency", default=lambda self:self.env.user.company_id.currency_id)
  base = fields.Float(string="Base price", help="Price of products", compute="_getBasePrice", store=True)
  iva = fields.Integer(string="Increment IVA")
  total = fields.Float(string="Price", help="The total price of the invoice", compute="_getTotalPrice", store=True)
  state = fields.Boolean()
  lines = fields.One2many("restaurapp_app.orderLine_model", "quantity", string="Lines", required=True)

  @api.depends("lines")
  def _getBasePrice(self):
    self.price = 0
    for line in self.lines:
      self.price += line.quantity * line.product_id.price

  @api.depends("base", "iva")
  def _getTotalPrice(self):
    self.total = self.base * (self.iva/100) + self.base