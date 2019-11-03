from odoo import fields, models, api
class list_item(models.Model):
    _name = 'todo.item'
    _description = 'Each item will be stored here...'
    name = fields.Char('Item', required=True)
    done = fields.Boolean('Done?', default=False)
    explanation = fields.Char('examplanation')
    person = fields.Many2many('todo.person', string='person')
    time_to_compleate =  fields.Date(default = "2019-12-01")