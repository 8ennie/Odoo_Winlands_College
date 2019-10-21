# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeAcademicStaff(models.Model):
    _name = 'college.staff.academic'
    _description = 'A class for Academic Staff Members at winelands college'

    #Relationships
    partner_id = fields.Many2one('college.staff',delegate=True,
        ondelete='cascade',required=True)
    module_ids = fields.Many2many(comodel_name='college.module',
        string = 'Modules Lectured')

    #Attributes
    #here
    amount_of_modules_lectured = fields.Integer(store=False, compute='_classes_lectured')

    #DemieFields

    @api.model
    def create(self, vals):
        vals['pType'] = "Academic"
        res = super().create(vals)
        return res

    @api.depends('module_ids')
    def _classes_lectured(self):
        for staff in self:
            for classes in staff.module_ids:
                for i in classes:
                    staff.amount_of_modules_lectured += 1
