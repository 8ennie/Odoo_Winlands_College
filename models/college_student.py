# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'A class for Students at winelands college'

    #Relationships
    partner_id = fields.Many2one('res.partner',delegate=True,
        ondelete='cascade',required=True)
    student_modules = fields.One2many('college.enrolledstudent','student_id',
    string = 'Module ID')
    student_program = fields.Many2one('college.program', string = 'Program ID',
        ondelete='cascade')

    #Attributes
    start_year = fields.Integer('Starting year')
