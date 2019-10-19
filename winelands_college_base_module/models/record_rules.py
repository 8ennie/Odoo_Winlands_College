from odoo import models, fields, api

class MyIrRule(models.Model):
    _inherit ="ir.rule"

    @api.model
    def _eval_context(self):
        context = super(MyIrRule,self)._eval_context()
        context.update(function_of_ids=function_of_ids)


    def function_of_ids(self):
        
