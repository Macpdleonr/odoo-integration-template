from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
     
    UserName = fields.Char(
        string="UserName",
        help="Username",
        config_parameter="username"
    )

    password = fields.Char(
        string="Password",
        help="Password",
        config_parameter="password"
    )
     
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        ICPSudo = self.env['ir.config_parameter'].sudo()

        username = ICPSudo.get_param('username')
        password = ICPSudo.get_param('password')

        res.update(
            username = username or '',
            password = '*' * (len(password) if password else 0) if password else ''
        )

        return res
     
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()

        if self.password and \
           self.password != '*' * len(self.password):
            ICPSudo.set_param('password', self.password)
            
            
        ICPSudo.set_param('username', self.username)