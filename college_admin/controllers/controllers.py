# -*- coding: utf-8 -*-
from odoo import http

# class ./custom-addons/winlandsCollegeManagment/collegeAdmin(http.Controller):
#     @http.route('/./custom-addons/winlands_college_managment/college_admin/./custom-addons/winlands_college_managment/college_admin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./custom-addons/winlands_college_managment/college_admin/./custom-addons/winlands_college_managment/college_admin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./custom-addons/winlands_college_managment/college_admin.listing', {
#             'root': '/./custom-addons/winlands_college_managment/college_admin/./custom-addons/winlands_college_managment/college_admin',
#             'objects': http.request.env['./custom-addons/winlands_college_managment/college_admin../custom-addons/winlands_college_managment/college_admin'].search([]),
#         })

#     @http.route('/./custom-addons/winlands_college_managment/college_admin/./custom-addons/winlands_college_managment/college_admin/objects/<model("./custom-addons/winlands_college_managment/college_admin../custom-addons/winlands_college_managment/college_admin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./custom-addons/winlands_college_managment/college_admin.object', {
#             'object': obj
#         })