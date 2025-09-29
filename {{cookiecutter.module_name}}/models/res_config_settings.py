from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
     
    {{cookiecutter.module_name}}_userName = fields.Char(
        string="{{cookiecutter.module_title}} UserName",
        help="{{cookiecutter.module_title}} Username",
        config_parameter="{{cookiecutter.module_name}}.username"
    )

    {{cookiecutter.module_name}}_password = fields.Char(
        string="{{cookiecutter.module_title}} Password",
        help="{{cookiecutter.module_title}} Password",
        config_parameter="{{cookiecutter.module_name}}.password"
    )

    {{cookiecutter.module_name}}_base_url = fields.Char(
        string="{{cookiecutter.module_title}} Base URL",
        help="Root URL of the {{cookiecutter.module_title}} System.\n"
         "This will be used as the base to build all API endpoints.",
        config_parameter="{{cookiecutter.module_name}}.base_url"
    )
     
    @api.model
    def get_values(self):
        res = super().get_values()

        ICPSudo = self.env['ir.config_parameter'].sudo()

        password = ICPSudo.get_param('{{cookiecutter.module_name}}.password')

        res.update(
            {{cookiecutter.module_name}}_password = '*' * (len(password) if password else 0) if password else '',
        )

        return res
     
    def set_values(self):
        super().set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()

        if self.{{cookiecutter.module_name}}_password and \
           self.{{cookiecutter.module_name}}_password != '*' * len(self.{{cookiecutter.module_name}}_password):
            ICPSudo.set_param('{{cookiecutter.module_name}}.password', self.{{cookiecutter.module_name}}_password)