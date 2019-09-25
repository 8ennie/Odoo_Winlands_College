# -*- coding: utf-8 -*-
from odoo import http

# class ./custom-addons/winlandsCollegeManagment(http.Controller):
#     @http.route('/./custom-addons/winlands_college_managment/./custom-addons/winlands_college_managment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./custom-addons/winlands_college_managment/./custom-addons/winlands_college_managment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./custom-addons/winlands_college_managment.listing', {
#             'root': '/./custom-addons/winlands_college_managment/./custom-addons/winlands_college_managment',
#             'objects': http.request.env['./custom-addons/winlands_college_managment../custom-addons/winlands_college_managment'].search([]),
#         })

#     @http.route('/./custom-addons/winlands_college_managment/./custom-addons/winlands_college_managment/objects/<model("./custom-addons/winlands_college_managment../custom-addons/winlands_college_managment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./custom-addons/winlands_college_managment.object', {
#             'object': obj
#         })