# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import json
from odoo import models, fields, api
from odoo.http import json,request,Response

class Restaurapp(http.Controller):
                                                        #PRODUCTS#
    @http.route('/restaurapp_app/product', auth='public',type="http")
    def product(self, **kw):
        validata = http.request.env["restaurapp_app.product_model"].sudo().search_read([],["name","description","photo", "currency_id", "price", "category", "ingredients"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/restaurapp_app/getProduct','/restaurapp_app/getProduct/<int:prodid>'],auth='public', type='http')
    def getProduct(self,prodid=None, **kw):
        if prodid:
            domain = [("id","=",prodid)]
        else:
            domain=[]
        taskdata = http.request.env["restaurapp_app.product_model"].sudo().search_read(domain,["name","description","price", "category"])
        data={  "status":200,
            "data":taskdata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/addProduct',auth='public', type='json',method="POST")
    def addProduct(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["restaurapp_app.product_model"].sudo().create(response)
            data = {"status":201, "id":result.id}
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/updateProduct',auth='public', type='json',method="PUT")
    def updateProduct(self, **kw):
        response = request.jsonrequest
        try:
            productdata = http.request.env["restaurapp_app.product_model"].sudo().search([("id","=",response["id"])])
            productdata.sudo().write(response)
            data={  
                "status":200,
                "data":productdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/delProduct',auth='public', type='json',method="DELETE")
    def delProduct(self, **kw):
        response = request.jsonrequest
        try:
            productdata = http.request.env["task_app.task_model"].sudo().search([("id","=",response["id"])])
            productdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

                                                        #CATEGORY#
    @http.route('/restaurapp_app/category', auth='public',type="http")
    def category(self, **kw):
        validata = http.request.env["restaurapp_app.category_model"].sudo().search_read([],["name","product"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    http.route(['/restaurapp_app/getCategory','/restaurapp_app/getCategory/<int:categoryid>'],auth='public', type='http')
    def getCategory(self,categoryid=None, **kw):
        if categoryid:
            domain = [("id","=",categoryid)]
        else:
            domain=[]
        categorydata = http.request.env["restaurapp_app.category_model"].sudo().search_read(domain,["name", "product"])
        data={  
            "status":200,
            "data":categorydata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/addCat',auth='public', type='json',method="POST")
    def addCat(self, **kw):
        response = request.jsonrequest
        try:
            categorydata = http.request.env["restaurapp_app.category_model"].sudo().create(response)
            data={  
                "status":201,
                "data":categorydata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/updateCat',auth='public', type='json',method="PUT")
    def updateCat(self, **kw):
        response = request.jsonrequest
        try:
            categorydata = http.request.env["restaurapp_app.category_model"].sudo().search([("id","=",response["id"])])
            categorydata.sudo().write(response)
            data={  
                "status":200,
                "data":categorydata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/delCat',auth='public', type='json',method="DELETE")
    def delCat(self, **kw):
        response = request.jsonrequest
        try:
            categorydata = http.request.env["restaurapp_app.category_model"].sudo().search([("id","=",response["id"])])
            categorydata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

                                                        #INGREDIENTS#
    @http.route('/restaurapp_app/ingredients', auth='public',type="http")
    def ingredients(self, **kw):
        validata = http.request.env["restaurapp_app.ingredients_model"].sudo().search_read([],["name","description", "product"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/restaurapp_app/getIngredients','/restaurapp_app/getIngredients/<int:ingredientsid>'],auth='public', type='http')
    def getIngredients(self,ingredientsid=None, **kw):
        if ingredientsid:
            domain = [("id","=",ingredientsid)]
        else:
            domain=[]
        taskdata = http.request.env["restaurapp_app.ingredients_model"].sudo().search_read(domain,["name","description","product"])
        data={  "status":200,
            "data":taskdata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/addIngredients',auth='public', type='json',method="POST")
    def addIngredients(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["restaurapp_app.ingredients_model"].sudo().create(response)
            data = {"status":201, "id":result.id}
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/updateIngredients',auth='public', type='json',method="PUT")
    def updateIngredients(self, **kw):
        response = request.jsonrequest
        try:
            ingredientsdata = http.request.env["restaurapp_app.ingredients_model"].sudo().search([("id","=",response["id"])])
            ingredientsdata.sudo().write(response)
            data={  
                "status":200,
                "data":ingredientsdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/delIngredients',auth='public', type='json',method="DELETE")
    def delIngredients(self, **kw):
        response = request.jsonrequest
        try:
            ingredientdata = http.request.env["restaurapp_app.ingredients_model"].sudo().search([("id","=",response["id"])])
            ingredientdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

                                                        #ORDER#
    @http.route('/restaurapp_app/order', auth='public',type="http")
    def order(self, **kw):
        validata = http.request.env["restaurapp_app.order_model"].sudo().search_read([],["table", "clients", "waiter", "pax", "tPrice", "orderLine"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/restaurapp_app/getOrder','/restaurapp_app/getOrder/<int:orderid>'],auth='public', type='http')
    def getOrder(self,orderid=None, **kw):
        if orderid:
            domain = [("id","=",orderid)]
        else:
            domain=[]
        
        orderdata = http.request.env["restaurapp_app.order_model"].sudo().search_read(domain,["table","waiter","pax", "clients", "tPrice", "orderLine"])
        data={  "status":200,
            "data":orderdata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/addOrder',auth='public', type='json',method="POST")
    def addOrder(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["restaurapp_app.order_model"].sudo().create(response)
            data = {"status":201, "id":result.id}
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/updateOrder',auth='public', type='json',method="PUT")
    def updateOrder(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurapp_app.order_model"].sudo().search([("id","=",response["id"])])
            orderdata.sudo().write(response)
            data={  
                "status":200,
                "data":orderdata.id
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

    @http.route('/restaurapp_app/delOrder',auth='public', type='json',method="DELETE")
    def delOrder(self, **kw):
        response = request.jsonrequest
        try:
            orderdata = http.request.env["restaurapp_app.order_model"].sudo().search([("id","=",response["id"])])
            orderdata.sudo().unlink()
            data={  
                "status":200,
                }
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data

                                                    #INVOICE#

    @http.route('/restaurapp_app/invoice', auth='public',type="http")
    def invoice(self, **kw):
        validata = http.request.env["restaurapp_app.invoice_model"].sudo().search_read([],["ref", "date", "base", "iva", "total", "lines", "client"])
        data ={"status":200, "data":validata}
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route(['/restaurapp_app/getInvoice','/restaurapp_app/getInvoice/<int:invoiceid>'],auth='public', type='http')
    def getInvoice(self,invoiceid=None, **kw):
        if invoiceid:
            domain = [("id","=",invoiceid)]
        else:
            domain=[]
        invoicedata = http.request.env["restaurapp_app.invoice_model"].sudo().search_read(domain,["ref", "date", "base", "iva", "total", "lines", "client"])
        for rec in invoicedata:
            rec["date"] = rec["date"].isoformat()
        data={  "status":200,
            "data":invoicedata 
            }
        return http.Response(json.dumps(data).encode("utf8"),mimetype="application/json")

    @http.route('/restaurapp_app/addInvoice',auth='public', type='json',method="POST")
    def addInvoice(self, **kw):
        response = request.jsonrequest
        try:
            result = http.request.env["restaurapp_app.invoice_model"].sudo().create(response)
            data = {"status":201, "id":result.id}
            return data
        except Exception as e:
            data={  
                "status":404,
                "error":e 
                }
            return data
    

    @http.route(['/restaurapp_app/confirmInvoice/<int:id>'], auth='public', type="http")
    def confirmInvoice(self, id=None, **kw):
        order = http.request.env["restaurapp_app.order_model"].sudo().search([("id", "=", id)])
        order.confirmInvoice()
        data = { "status":200 }
        return http.Response(json.dumps(data).encode("utf8"), mimetype="application/json")