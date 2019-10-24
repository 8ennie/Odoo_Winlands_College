# -*- coding: utf-8 -*-
{
    'name': "Winelands College Result Managment",

    'summary': """
            A Module to manage all the student marks at Winelands College
        """,

    'description': """
            The Module is intended for academic staff, to upload student marks and for student to view there marks
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
    'depends': ['base', 'winelands_college_base_module', 'college_admin'],

    # always loaded
    'data': [
        'views/results_menu.xml',
        'views/module_view.xml',
        'views/marks_view.xml',
        'views/student_transcript.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
