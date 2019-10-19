# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeProgram(models.Model):
    _name = 'college.program'
    _description = 'A class for different programes at winlands college'

    #Relationships
    module_id = fields.One2many('college.module','program_id',
        string = 'Module ID')
    module_id = fields.One2many('college.student','program_id',
        string = 'Student ID')

    #Attributes
    name = fields.Char('Name')
    length = fields.Integer('Length')
    qualification = fields.Selection([('',''),],string='Qualification')
