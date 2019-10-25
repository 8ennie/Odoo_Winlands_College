# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api
import datetime


class CollegeEnrolledStudent(models.Model):
    _name = 'college.enrolledstudent'
    _description = 'A class to map Students and Modules at winelands college'
    _rec_name = 'compued_name'

    #Relationships
    student_id = fields.Many2one('college.student', string = 'Student ID',
        ondelete='cascade',required=True)
    module_id = fields.Many2one('college.module', string = 'Module ID',required=True)

    #Attributes
    compued_name = fields.Char(compute = 'compute_name_for_enrolled_student',store=False)
    year = fields.Char('Year', size=4,default= str(datetime.datetime.now().year))
    _sql_constraints = [ ('Module_and_year_unique','UNIQUE (module_id,year,student_id)', 'This module and the year need to be unique'), ]

    @api.depends('student_id')
    def compute_name_for_enrolled_student(self):
        for enrolledstudent in self:
            enrolledstudent.compued_name = enrolledstudent.student_id.name + " in " + enrolledstudent.module_id.name

    @api.constrains("year")
    def check_the_year(self):
        for value in self:
            if len(value.year)!= 4:
                raise ValidationError("This is not an appropriate year")
            if(int(value.year)-int(datetime.datetime.now().year)>5):
                raise ValidationError("The date is greater then 5 year from the current date")
