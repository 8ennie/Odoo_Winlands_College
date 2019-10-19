# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeStaff(models.Model):
    _name = 'college.staff'
    _description = 'An abstract class for Staff Members at winelands college'

    #Relationships
    partner_id = fields.Many2one('res.partner',delegate=True,
        ondelete='cascade',required=True)
    department_id = fields.Many2one('college.department', string = 'Department ID',
        ondelete='cascade', required=True)

    #Attributes
    staff_email = fields.Char('Staff Email Adress')
