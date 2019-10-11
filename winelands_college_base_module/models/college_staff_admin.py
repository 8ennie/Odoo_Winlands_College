# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeAdminStaff(models.Model):
    _name = 'college.staff.admin'
    _description = 'A class for Administartive Staff Members at winelands college'

    #Relationships
    partner_id = fields.Many2one('college.staff',delegate=True,
        ondelete='cascade',required=True)

    #Attributes