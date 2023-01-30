# -*- coding: utf-8 -*-
{
    'name': "restaurapp_app",

    'summary': """
        Application to control the bar or restaurant""",

    'description': """
        This application control the bar or restaurant
    """,

    'author': "Rafa De la Haba",
    'website': "http://www.isca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/category_view.xml',
        'views/ingredients_view.xml',
        'views/order_view.xml',
        'views/orderLine_view.xml',
        'views/invoice_view.xml',
        'views/invoiceLine_view.xml',
        'views/invoicePDF.xml',
        'views/menu.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
