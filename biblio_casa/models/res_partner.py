from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_socio_casa = fields.Boolean(string='Es Socio', default=False)
    es_escritor_casa = fields.Boolean(string='Es Escritor', default=False)
