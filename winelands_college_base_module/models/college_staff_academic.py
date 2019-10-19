# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeAcademicStaff(models.Model):
    _name = 'college.staff.academic'
    _description = 'A class for Academic Staff Members at winelands college'

    #Relationships
    partner_id = fields.Many2one('college.staff',delegate=True,
        ondelete='cascade',required=True)
    lectured_classes = fields.One2many('college.lecturedclasses','acadenic_staff_id',
    string = 'Lectured Classes ID')

    #Attributes


    #DemieFields



    @api.model
    def create(self, vals):
        vals['pType'] = "Academic"
        res = super().create(vals)
        return res
