# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'A class for different departments at winlands college'

    #Relationships
    staff_id = fields.One2many('college.staff','department_id',
    string = 'Department ID')
    module_id = fields.One2many('college.module','department_id',
    string = 'Module ID')

    #Attributes
    name = fields.Char('Name')
