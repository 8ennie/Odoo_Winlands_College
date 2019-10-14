# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeModule(models.Model):
    _name = 'college.module'
    _description = 'A class for different modules at winlands college'

    #Relationships
    module_students = fields.One2many('college.enrolledstudent','module_id',
        string = 'Student ID')

    #Attributes
    module_name = fields.Char('Name')
        #the time in quaters that the modules have (2 Quaters = 1 Semester)
    module_time_frame = fields.Integer('Timeframe')
    module_credits = fields.Integer('Credits')
