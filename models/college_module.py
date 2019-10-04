# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeModule(models.Model):
    _name = 'college.module'
    _description = 'A class for different modules at winlands college'

    #Relationships
    module_students = field.One2many('college_enrolled_student','module_id',
        string = 'Student ID')

    #Attributes
    module_name = field.Char()
        #the time in quaters that the modules have (2 Quaters = 1 Semester)
    module_time_frame = field.Integer()
    module_creadits = field.Integer()
