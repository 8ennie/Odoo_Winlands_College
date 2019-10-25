from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    #Relationships

    #Attributes
    email = fields.Char(compute='_compute_email');

    #DemieFields
    create_user = fields.Boolean(store=False, default=True, string="Do You want to create a User")
    pType = fields.Char(store=False)

    @api.model
    def create(self, vals):
        print(vals)
        res = super().create(vals)
        if vals['create_user'] is True:
            user = self.env['res.users'].create({'login' : res.email,'password' : "password",'partner_id' : res.id})
            #for students
            if vals['pType'] is 'Student':
                group = self.env['res.groups'].search([('id', '=', self.env.ref('winelands_college_base_module.winelands_group_student').id)])
                group.write({'users': [(4, user.id)]})
            #for admin
            elif vals['pType'] is 'Admin':
                group = self.env['res.groups'].search([('id', '=', self.env.ref('winelands_college_base_module.winelands_group_admin_staff').id)])
                group.write({'users': [(4, user.id)]})
            #for academic
            elif vals['pType'] is 'Academic':
                group = self.env['res.groups'].search([('id', '=', self.env.ref('winelands_college_base_module.winelands_group_academic').id)])
                group.write({'users': [(4, user.id)]})
        return res

    def _compute_email(self):
        for partner in self:
            partner.email = str(partner.id) + "@cwc.ac.za"
