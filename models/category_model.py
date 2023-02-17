from odoo import models, fields, api


class category(models.Model):
    _name = 'restaurapp_app.category_model'
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(string="Name", help="Name of the category", required=True, index=True)
    complete_name = fields.Char('Complete name', compute='_compute_complete_name', recursive=True, store=True)
    product = fields.One2many("restaurapp_app.product_model", inverse_name="category",string="Product")
    parent_id = fields.Many2one("restaurapp_app.category_model", string="Parent Category", index=True, ondelete="cascade")
    child_id = fields.One2many("restaurapp_app.product_model", inverse_name="category",string="Product")

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s/%s' %(category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name
    