from datetime import datetime
from odoo import models, fields, api


class invoice(models.Model):
  _name = 'restaurapp_app.invoice_model'
  _description = 'This is the invoice model'
  _rec_name = 'ref'

  ref = fields.Integer(string="Invoice reference: ", help="Number of the invoice", default=lambda self: self.setRef(), readonly="True")
  date = fields.Date(string="Date: ", help="Description of the invoice", required=True, default=lambda self: datetime.now())
  base = fields.Float(string="Base price", help="Price of products", compute="_getBasePrice", store=True)
  iva = fields.Integer(string="Increment IVA", selection=[("0",'0%'), ("4",'4%'), ("10",'10%'), ("21",'21%')], default=10)
  total = fields.Float(string="Price", help="The total price of the invoice", compute="_getTotalPrice", store=True)
  state = fields.Selection(string="State: ", selection=[('D', 'Draft'), ('C', 'Confirmed')], default="D")
  lines = fields.One2many("restaurapp_app.il_model", "lineId", string="Lines: ")
  client = fields.Char("Client: ", help="Name of client", required=True)

  @api.depends("lines")
  def _getBasePrice(self):
    self.base = 0
    for line in self.lines:
      self.base += line.quantity * line.product.price

  @api.depends("base", "iva")
  def _getTotalPrice(self):
    self.total = self.base * (self.iva/100) + self.base

  def changeState(self):
    for record in self:
      record.state = 'C'

  def setRef(self):
    result = self.env['restaurapp_app.invoice_model'].search_read()
    if len(result) == 0:
      return 1
    else:
      return result[-1]["ref"] +1