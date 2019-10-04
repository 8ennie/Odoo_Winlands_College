# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'A class for Students at winelands college'

    #Relationships
    partner_id = fields.Many2one('res.partner',delegate=True,
        ondelete='cascade',required=True)

    #Attributes
    start_year = field.Integer()
