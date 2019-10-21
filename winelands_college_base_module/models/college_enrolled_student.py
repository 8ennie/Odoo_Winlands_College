# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api
import datetime
from fpdf import FPDF

class CollegeEnrolledStudent(models.Model):
    _name = 'college.enrolledstudent'
    _description = 'A class to map Students and Modules at winelands college'

    #Relationships
    student_id = fields.Many2one('college.student', string = 'Student ID',
        ondelete='cascade')
    module_id = fields.Many2one('college.module', string = 'Module ID')
    #Attributes
    year = fields.Char('Year', size=4,default= str(datetime.datetime.now().year))
    mark = fields.Float('Mark')

    
    @api.constrains('mark')
    def _mark_validation(self):
        for value in self:
            if value.mark>100:
                raise ValidationError("Mark may not be over 100, as it is a percentage")
            if value.mark<0:
                raise ValidationError("The mark may not be negitive")

    # def create_pdf(list_of_results,id_wcw):
    #     pdf = FPDF(orientation='P', unit='mm', format='A4')
    #     pdf.add_page()
    #     pdf.set_font("Arial", size=30)
    #     pdf.set_text_color(255,0,0)  
    #     pdf.cell(2, 10, txt= "Not for official purposes", ln=100, align = "l")
    #     heading_text =  "wine lands collage academic record for student: " + str(id_wcw)
    #     pdf.set_font("Arial", size=20)
    #     pdf.set_text_color(0,0,0) 
    #     pdf.cell(2, 20, txt=heading_text , ln=100, align = "l")
    #     pdf.set_font("Arial", size=20)
    #     pdf.set_text_color(0,0,0) 
    #     for mark in list_of_results:
    #         pdf.cell(2, 10, txt= mark, ln=100, align = "l")
    #     pdf.output("Academic_Transcript_"+str(id_wcw)+".pdf")
    # create_pdf(['hey','hey'], 23)

