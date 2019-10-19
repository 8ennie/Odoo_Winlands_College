# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CollegeProgram(models.Model):
    _name = 'college.program'
    _description = 'A class for different programes at winlands college'

    #Relationships
    module_id = fields.One2many('college.module','program_id',
        string = 'Module ID')
    student_id = fields.One2many('college.student','program_id',
        string = 'Student ID')

    #Attributes
    name = fields.Char('Name')
    length = fields.Integer('Length', help = 'How many years is this program')
    qualification = fields.Selection([('Higher Certificate','Higher Certificate'),('National Certificate','National Certificate'),('National Higher Certificate','National Higher Certificate'),('Advanced Certificate','Advanced Certificate'),('Diploma, Higher Diploma, National Diploma & Advanced Diploma','Diploma, Higher Diploma, National Diploma & Advanced Diploma'),('Baccalaureus Technologiae (B Tech)','Baccalaureus Technologiae (B Tech)'),('Bachelor’s Degree','Bachelor’s Degree'),('Postgraduate Certificate and Diploma','Postgraduate Certificate and Diploma'),('Honours Degree','Honours Degree'),('Magister Technologiae (M Tech)','Magister Technologiae (M Tech)'),('Master’s Degree','Master’s Degree'),('Doctor Technologiae (D Tech) and Doctoral Degree','Doctor Technologiae (D Tech) and Doctoral Degree')],string='Qualification')
    #qualification = fields.Selection([('',''),],string='Qualification')
