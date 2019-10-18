from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    email = fields.Char(compute='_compute_email');
    create_user = fields.Boolean(compute='_compute_create_user', store= 'False', default = "True", string="Do You want to create a User")

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.create_user is True:
            user = self.env['res.users'].create({'login' : res.email,'password' : "password",'partner_id' : res.id})

            #for students
            group = self.env['res.groups'].search([('id', '=', self.env.ref('winelands_college_base_module.winelands_group_student').id)])
            group.write({'users': [(4, user.id)]})
        return res

    def _compute_email(self):
        for partner in self:
            partner.email = str(partner.id) + "@cwc.ac.za"

    def _compute_create_user(self):
        a = "aasd"
