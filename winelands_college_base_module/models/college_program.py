# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api

class CollegeProgram(models.Model):
    _name = 'college.program'
    _description = 'A class for different programes at winlands college'

    #Relationships
    module_ids = fields.Many2many(comodel_name='college.module',
        string = 'Modules')
    student_id = fields.One2many('college.student','program_id',
        string = 'Students')

    #Attributes
    name = fields.Char('Name',required=True)

    @api.constrains('name')
    def _constrain_name_check(self):
        for value in self:
            if not value.name:
                raise ValidationError("This field cannot be left empty")

    length = fields.Integer('Length', help = 'How many years is this program')
    @api.constrains("length")
    def _check_length(self):
        for value in self:
            if value.length<=0:
                raise ValidationError("The years (length) may not be less zero")
            if value.length>=10:
                raise ValidationError("The program may not be longer then 10 years")

    qualification = fields.Selection([('NA','Not Applicable'),('Higher Certificate','Higher Certificate'),('National Certificate','National Certificate'),('National Higher Certificate','National Higher Certificate'),('Advanced Certificate','Advanced Certificate'),('Diploma, Higher Diploma, National Diploma & Advanced Diploma','Diploma, Higher Diploma, National Diploma & Advanced Diploma'),('Baccalaureus Technologiae (B Tech)','Baccalaureus Technologiae (B Tech)'),('Bachelor’s Degree','Bachelor’s Degree'),('Postgraduate Certificate and Diploma','Postgraduate Certificate and Diploma'),('Honours Degree','Honours Degree'),('Magister Technologiae (M Tech)','Magister Technologiae (M Tech)'),('Master’s Degree','Master’s Degree'),('Doctor Technologiae (D Tech) and Doctoral Degree','Doctor Technologiae (D Tech) and Doctoral Degree')],string='Qualification')
    @api.constrains("qualification")
    def _check_valid(self):
        for value in self:
            if not value.qualification:
                raise ValidationError("A Qualification must be selected, select not applicable, if no option is available")
