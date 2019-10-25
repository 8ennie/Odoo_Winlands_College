from odoo import models, fields, api
from odoo.exceptions import ValidationError
class CollegeMarks(models.Model):
    _name = 'college.marks'
    _description = 'A class for Student Marks at winelands college'
    _rec_name = 'odoo_name_field'

    #Relationships
    enrolled_students_id = fields.Many2one('college.enrolledstudent',delegate=True,
        ondelete='cascade',required=True)

    #Attributes
    odoo_name_field = fields.Char(compute ='compute_name_for_mark', store= False)
    mark = fields.Float('Mark')

    @api.constrains('mark')
    def _mark_validation(self):
        for value in self:
            if value.mark>100:
                raise ValidationError("Mark may not be over 100, as it is a percentage")
            if value.mark<0:
                raise ValidationError("The mark may not be negitive")

    @api.depends('enrolled_students_id')
    def compute_name_for_mark(self):
        for mark in self:
            mark.odoo_name_field = mark.enrolled_students_id.student_id.name + "s mark for " + mark.enrolled_students_id.module_id.name
