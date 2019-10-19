# -*- coding: utf-8 -*-
{
    'name': "Winelands College Admin",

    'summary': """
        A Module to manage all entaties at Winelands Colleege
        """,

    'description': """
        A Module to manage Staff personal, Students, Departmets, Modules for the Winelands College
    """,

    'application': True,

    'author': "23725648; 20456395; 21071926; 19772815",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'winelands_college_base_module'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/admin_menu.xml',
        'views/module_view.xml',
        'views/student_view.xml',
        'views/academic_staff_view.xml',
        'views/department_view.xml',
        'views/program_view.xml',
        'views/admin_staff_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
