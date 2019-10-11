# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeAcademicStaff(models.Model):
    _name = 'college.staff.academic'
    _description = 'A class for Academic Staff Members at winelands college'

    #Relationships
    partner_id = fields.Many2one('college.staff',delegate=True,
        ondelete='cascade',required=True)

    #Attributes
