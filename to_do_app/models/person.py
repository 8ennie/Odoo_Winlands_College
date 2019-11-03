from odoo import fields, models, api
import random
class person_item(models.Model):
    _name = 'todo.person'
    _description = 'Each person will be stored here'
    _order = 'per_id desc'
    name = fields.Char('Name', required=True) 
    mail = fields.Char('mail', default = "info@example.com")
    item = fields.Many2many('todo.item', string='item')
    per_id = fields.Char(compute = "_get_a_random", store = True)

    @api.multi
    def button_do_somthing(self):
        self.mail = self.name+"@erp_industries.com"
    
    @api.depends("name")
    def _get_a_random(self):
        for values in self:
            num = random.randint(11111,999999)
            values.per_id = str(num)

sql_constraints = [('make_sure_id_is_righg', 'UNIQUE (per_id)', "Retry the save button")]
