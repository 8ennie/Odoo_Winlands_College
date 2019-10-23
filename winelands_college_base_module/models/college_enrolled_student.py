# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api
#from fpdf import FPDF
#from gtts import gTTS
import datetime


class CollegeEnrolledStudent(models.Model):
    _name = 'college.enrolledstudent'
    _description = 'A class to map Students and Modules at winelands college'
    _rec_name = 'compued_name'

    #Relationships
    student_id = fields.Many2one('college.student', string = 'Student ID',
        ondelete='cascade')
    module_id = fields.Many2one('college.module', string = 'Module ID')

    #Attributes
    compued_name = fields.Char(compute = 'compute_name_for_enrolled_student',store=False)
    year = fields.Char('Year', size=4,default= str(datetime.datetime.now().year))

    @api.depends('student_id')
    def compute_name_for_enrolled_student(self):
        for enrolledstudent in self:
            enrolledstudent.compued_name = enrolledstudent.student_id.name + " in " + enrolledstudent.module_id.name

    # def create_pdf(list_of_results,id_wcw):
    #     pdf = FPDF(orientation='P', unit='mm', format='A4')
    #     pdf.add_page()
    #     pdf.set_font("Arial", size=30)
    #     pdf.set_text_color(255,0,0)
    #     pdf.cell(2, 10, txt= "Not for official purposes", ln=100, align = "l")
    #     heading_text =  "Winelands college academic record for student: " + str(id_wcw)
    #     pdf.set_font("Arial", size=20)
    #     pdf.set_text_color(0,0,0)
    #     pdf.cell(2, 20, txt=heading_text , ln=100, align = "l")
    #     pdf.set_font("Arial", size=20)
    #     pdf.set_text_color(0,0,0)
    #     for mark in list_of_results:
    #         pdf.cell(2, 10, txt= mark, ln=100, align = "l")
    #     pdf.output("Academic_Transcript_"+str(id_wcw)+".pdf")
    # create_pdf(['hey','hey'], 23)

    # def create_audio(ist_of_results,id_wcw):
    #     convert = "For sudent " + str(id_wcw) + " here are the results."
    #     for i in ist_of_results:
    #         convert+= " " + i + " "
    #     tts = gTTS(text=convert, lang='en')
    #     tts.save("audio.mp3")
    # create_audio(['hey','hey'], 23)
