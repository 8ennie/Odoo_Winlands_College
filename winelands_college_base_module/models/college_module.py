# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class CollegeModule(models.Model):
    _name = 'college.module'
    _description = 'A class for different modules at winlands college'

    #Relationships
    module_students = fields.One2many('college.marks','module_id',
        string = 'Studensts')
    department_id = fields.Many2one('college.department', string = 'Department ID',
        ondelete='cascade')
    staff_ids = fields.Many2many(comodel_name='college.staff.academic',
        string = 'Module Lecturers')
    program_ids = fields.Many2many(comodel_name='college.program',
        string = 'Programs')

    #Computed Attributes
    amount_of_students = fields.Integer(store=False, compute='_compute_number_of_students')

    @api.depends("module_students")
    def _compute_number_of_students(self):
        for program in self:
            for students in program.module_students:
                program.amount_of_students += 1

    #Attributes
    name = fields.Char('Name',required=True)
        #the time in quaters that the modules have (2 Quaters = 1 Semester)
    time_frame = fields.Integer('Timeframe',help="Number of Quaters the Module tackes \n ([2] => Two Quaters => One Semester)")
    credits = fields.Integer('Credits',required=True)

    @api.constrains('name')
    def _check_name(self):
          for value in self:
            if not value.name:
                raise ValidationError("The name field cannot be left empty")

    @api.constrains('time_frame')
    def _check_time_frame(self):
        for value in self:
            if value.time_frame>4:
                raise ValidationError("The module may not be longer then a year\nNumber of Quaters the Module tackes \n ([2] => Two Quaters => One Semester)")
            if value.time_frame<=0:
                raise ValidationError("The time may not be less then 1 term")

    @api.constrains("credits")
    def _check_credits(self):
        for value in self:
            if value.credits<=0:
                raise ValidationError("The amount of credits may not be less then zero")
