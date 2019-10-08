# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ./custom-addons/winlands_college_managment/college_admin(models.Model):
#     _name = './custom-addons/winlands_college_managment/college_admin../custom-addons/winlands_college_managment/college_admin'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100