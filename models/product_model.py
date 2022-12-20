from odoo import models, fields, api


class product(models.Model):
  _name = 'restaurapp_app.product_model'
  _description = 'This is the product model'

  name = fields.Char(string="Product Name", help="Name of the product", required=True, index=True)
  description = fields.Html(string="Description", help="Description of the product", required=True)
  photo = fields.Image(string="Photo")
  currency_id = fields.Many2one('res.currency', string="Curency", default=lambda self:self.env.user.company_id.currency_id)
  price = fields.Monetary(string="Price")
  category = fields.Many2one("restaurapp_app.category_model", string="Category")
  ingredients = fields.Many2many("restaurapp_app.ingredients_model",string="Ingredients",relation="ingredients2products")
  












 #   def generatePassword(self):
 #     letters = string.ascii_letters
 #     digits = string.digits
 #     alphabet = letters + digits
 #     pwd_length = 12
 #     pwd = ' '
 #     for i in range(pwd_length):
 #       pwd += ''.join(secrets.choice(alphabet))
 #     self.password = pwd

    #datefinished = fields.Datetime(string="Date Finished", help="The date of task is finished")
    #active = fields.Boolean(string="Is the task active?", help="The task is active?", default=True)
    #resp = fields.Char(string="Responsible", help="The responsable of the task")
    
    #@api.onchange("isdone")
    #def changeActiveTask(self):
     #   self.active = not self.isdone
      #  self.isdone = not self.active
      #  if self.isdone:
      #      self.datefinished = datetime.now()
      #      self.resp = self.env.user.name
      #      self.active = False
            
 
    #def changeState(self):
    #    self.ensure_one()
    #    self.isdone = not self.isdone
    #    self.active = not self.isdone


    #def cleanFinished(self):
    #    records = self.search([("active","=",False)])
    #    for rec in records:
    #        rec.unlink()