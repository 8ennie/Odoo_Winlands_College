from odoo import fields, models, api
from odoo.exceptions import ValidationError, MissingError
import random

class list_dependent(models.Model):
    _name = 'todo.dependent'
    _description = 'Each item will be stored here...'
    name = fields.Char('Name', required=True)
    person = fields.Many2many('todo.person',string='name')
    initials = fields.Char(compute = "_compute_initials", store = False)
    randomFact = fields.Char(compute = "_compute_fact", store = False, String = "Random Facts")
    # what is it usiing to depend on, so what value must chnage
    
    @api.multi
    def button_help(self):
        raise MissingError("THERE IS NOT HELP!!!")


    @api.depends("name")
    def _compute_fact(self):
        for values in self:
            facts = ["why do we yawn","apples can be red", "laptops are strange", "we talk less and less", "I love this world","iphones are really expensive","Can we just be freinds"]
            num = random.randint(0,len(facts)-1)
            values.randomFact = facts[num]

    @api.depends("name")
    def _compute_initials(self):
        for values in self:
            values.initials = values.name[0:2]
    

    @api.constrains('name')
    def _check_name(self):
        print("when working with this we must remeber the dot notation")
        for values in self:
            if values.name == "fuck":
                raise ValidationError("Don't even think about it!")
            if len(values.name)>20:
                raise ValidationError("For some reason it can not be longfer then 20")