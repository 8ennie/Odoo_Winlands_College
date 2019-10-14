# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeProgram(models.Model):
    _name = 'college.program'
    _description = 'A class for different programes at winlands college'

    #Relationships

    #Attributes
    name = fields.Char('Name')
    length = fields.Integer('Length')
    qualification = fields.Char('Qualification')
