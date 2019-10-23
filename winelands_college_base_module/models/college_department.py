# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class CollegeDepartment(models.Model):
    _name = 'college.department'
    _description = 'A class for different departments at winlands college'

    #Relationships
    staff_id = fields.One2many('college.staff','department_id',
    string = 'Staff ID')
    module_id = fields.One2many('college.module','department_id',
    string = 'Module ID')

    #Attributes
    name = fields.Char('Name')
    
    #checks
    @api.constrains('name')
    def _constrain_name_check(self):
        for value in self:
            if not value.name:
                raise ValidationError("This field cannot be left empty")

    #computed
    amount_of_staff = fields.Integer(store=False, compute='_compute_number_of_staff')

    @api.depends('staff_id')
    def _compute_number_of_staff(self):
        for department in self:
            for i in department.staff_id:
                department.amount_of_staff +=1

    _sql_constraints = [ ('name_must_be_unique','UNIQUE (name)', 'The department name already exists'), ]
   
    def get_users(self):
        domain = ('user.id', 'in', [(2),(3)])
        return domain
