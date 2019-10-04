# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeLecturedClasses(models.Model):
    _name = 'college.lecturedClasses'
    _description = 'A class to map AcademicStaff to Modules at winelands college'

    #Relationships
    acadenic_staff_id = fields.Many2one('college.staff.academic',
        string = 'AcademicStaf ID', ondelete='cascade')
    module_id = fields.Many2one('college.module', string = 'Module ID',
        ondelete='restricted')

    #Attributes
