# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CollegeStaff(models.Model):
    _name = 'college.staff'
    _description = 'An abstract class for Staff Members at winelands college'

    #Relationships
    partner_id = fields.Many2one('res.partner',delegate=True,
        ondelete='cascade',required=True)
    department_id = fields.Many2one('college.department', string = 'Department ID',
        ondelete='cascade', required=True)

    #Attributes
    staff_email = fields.Char('Staff Email Adress', compute = 'getSatffEmail')

    @api.depends('partner_id.name')
    @api.multi
    def getSatffEmail(self):
        for partner in self:
            staff_email = str(partner.name) + "@cwc.ac.za"
            __new_staff_email=""
            for c in staff_email:
                if c is " ":
                    continue
                __new_staff_email = __new_staff_email + c.lower()
            __new_staff_email.replace(" ", "")
            __new_staff_email.lower()
            print(__new_staff_email)
            partner.staff_email = __new_staff_email

    @api.constrains('department_id')
    def _department_validation(self):
        for staff in self:
            is_in_department = False
            for depStaff in staff.department_id.staff_id:
                if self.env.user.partner_id.id is depStaff.partner_id.id:
                    is_in_department = True
            if not is_in_department:
                raise ValidationError("You can only add Staff to your own Department!")
