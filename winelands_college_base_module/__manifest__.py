# -*- coding: utf-8 -*-
{
    'name': "Winelands College Base Module",

    'summary': """
         A module to manage, students and there marks at Winlands College""",

    'description': """
        A module to manage students and there marks in diffretn Modules.
    """,

    'application': True,

    'author': "23725648; 20456395; 21071926",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/winelands_security_base.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/college_menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
