from odoo import fields, models
class list_dependent(models.Model):
    _name = 'todo.dependent'
    _description = 'Each item will be stored here...'
    name = fields.Char('Name', required=True)
    jams = fields.Char('jams')
    person = fields.many2many(todo.person, 'name' ,string='name')
    #this is to check that it is right...

    # @api.constrains('name')
    # def _check_name(self):
    #     for name in self:
    #         print(name) 