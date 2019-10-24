from odoo import models, fields, api


class GetFile(models.TransientModel):

    _name = 'save.file.wizard'
    file_name = fields.Char('File name', readonly=True)
    my_file = fields.Binary('File data', readonly=True,
        help='File(jpg, csv, xls, exe, any binary or text format)')
