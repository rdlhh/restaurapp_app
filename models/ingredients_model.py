from odoo import models, fields, api

class ingredients(models.Model):
    _name = 'restaurapp_app.ingredients_model'
    _description = 'This is the ingredients model'

    name = fields.Char(string="Ingredient Name", help="Name of the ingredient", required=True, index=True)
    description = fields.Text(string="Description", help="Description of the ingredient")
    product = fields.Many2many("restaurapp_app.product_model",string="Products",relation="ingredients2products")