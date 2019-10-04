# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeProgram(models.Model):
    _name = 'college.program'
    _description = 'A class for different programes at winlands college'

    #Relationships

    #Attributes
    program_name = fields.Char('Name')
    program_length = fields.Integer('Length')
    program_qualification = fields.Char('Qualification')
