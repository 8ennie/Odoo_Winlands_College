# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeModule(models.Model):
    _name = 'college.module'
    _description = 'A class for different modules at winlands college'

    #Relationships
    module_students = fields.One2many('college.enrolledstudent','module_id',
        string = 'Student ID')
    department_id = fields.Many2one('college.department', string = 'Department ID',
        ondelete='cascade')
    program_id = fields.Many2one('college.program', string = 'Program ID',
        ondelete='cascade')
    lectured_classes = fields.One2many('college.lecturedclasses','module_id',
        string = 'Lectured Classes ID')

    #Attributes
    name = fields.Char('Name')
        #the time in quaters that the modules have (2 Quaters = 1 Semester)
    time_frame = fields.Integer('Timeframe',help="Number of Quaters the Module tackes \n ([2] => Two Quaters => One Semester)")
    credits = fields.Integer('Credits')


    def getModule(self):
        return  [('True','=',True)]
