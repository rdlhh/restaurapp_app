# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json

class Restaurapp(http.Controller):

    @http.route('/restaurapp_app/product', auth='public',type="http")
    def product(self, **kw):
        validata = http.request.env["restaurapp_app.product_model"].sudo().search_read([],["name","description","photo", "currency_id", "price", "category", "ingredients"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/category', auth='public',type="http")
    def category(self, **kw):
        validata = http.request.env["restaurapp_app.category_model"].sudo().search_read([],["name","product"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/ingredients', auth='public',type="http")
    def ingredients(self, **kw):
        validata = http.request.env["restaurapp_app.ingredients_model"].sudo().search_read([],["name","description", "product"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")


#    @http.route('/validations_app/hello', auth='public', type="http")
#    def hello(self, **kw):
#        return "Hello World!"

#    @http.route('/validations_app/test', auth='public',type="http")
#    def test(self, **kw):
#        validata = http.request.env["validations_app.students_model"].sudo().search_read([],["name","location"])
#        data ={"status":200, "data":validata}
#        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/jason")

#    @http.route('/validations_app/test', auth='public',type="http")
#    def test(self, **kw):
#        validata = http.request.env["validations_app.modules_model"].sudo().search_read([],["name"])
#        data ={"status":200, "data":validata}
#        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/jason")

# class TaskApp(http.Controller):
#     @http.route('/task_app/task_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_app/task_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_app.listing', {
#             'root': '/task_app/task_app',
#             'objects': http.request.env['task_app.task_app'].search([]),
#         })

#     @http.route('/task_app/task_app/objects/<model("task_app.task_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_app.object', {
#             'object': obj
#         })
