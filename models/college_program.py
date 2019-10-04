# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeProgram(models.Model):
    _name = 'college.program'
    _description = 'A class for different programes at winlands college'

    #Relationships

    #Attributes
    program_name = field.Char()
    program_length = field.Integer()
    program_qualification = field.Char()
