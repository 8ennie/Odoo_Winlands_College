# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class CollegeEnrolledStudent(models.Model):
    _name = 'college.enrolledstudent'
    _description = 'A class to map Students and Modules at winelands college'

    #Relationships
    student_id = fields.Many2one('college.student', string = 'Student ID',
        ondelete='cascade')
    module_id = fields.Many2one('college.module', string = 'Module ID')
    #Attributes
    year = fields.Char('Year', size=4,default= str(datetime.datetime.now().year))
    mark = fields.Float('Mark')
