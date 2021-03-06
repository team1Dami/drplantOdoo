# -*- coding: utf-8 -*-
{
    'name': "drplant",

    'summary': """
        Module that manages the shops""",

    'description': """
        Module that can create, modify and delete shops
    """,

    'author': "DrPlant",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/reports.xml',
        'security/security.xml',
        'security/ir.model.access.csv'

        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}