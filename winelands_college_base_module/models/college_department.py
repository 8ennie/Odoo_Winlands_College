# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'A class for different departments at winlands college'

    #Relationships

    #Attributes
    name = fields.Char('Name')
