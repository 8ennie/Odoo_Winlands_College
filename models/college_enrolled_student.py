# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeEnrolledStudent(models.Model):
    _name = 'college.enrolledStudent'
    _description = 'A class to map Students and Modules at winelands college'

    #Relationships
    student_id = fields.Many2one('college.student', string = 'Student ID',
        ondelete='cascade')
    module_id = fields.Many2one('college.module', string = 'Module ID',
        ondelete='restricted')

    #Attributes
    year = field.Integer()
    mark = fied.Float()
