# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'A class for Students at winelands college'

    #Relationships
    partner_id = fields.Many2one('res.partner',delegate=True,
        ondelete='cascade',required=True)
    student_modules = fields.One2many('college.enrolledstudent','student_id',
    string = 'Module ID')
    program_id = fields.Many2one('college.program', string = 'Program ID',
        ondelete='cascade')

    amount_of_credits = fields.Integer(store=False, compute='_compute_credits')

    #Attributes
    start_year = fields.Char('Starting Year',size=4,default = str(datetime.datetime.now().year))

    #DemieFields

    @api.depends('student_modules')
    def _compute_credits(self):
        for student in self:
            for marks in student.student_modules:
                student.amount_of_credits += marks.module_id.credits
                print(marks.module_id.credits)


    @api.model
    def create(self, vals):
        vals['pType'] = "Student"
        res = super().create(vals)
        return res
