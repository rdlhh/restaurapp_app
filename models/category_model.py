from odoo import models, fields, api


class category(models.Model):
    _name = 'restaurapp_app.category_model'

    name = fields.Char(string="Name", help="Name of the category", required=True, index=True)
    photo = fields.Binary(string="photo", help="Photo of product")
    product = fields.One2many("restaurapp_app.product_model", inverse_name="category",string="Product")
    