
from odoo import models, fields

#reusamos un modulo
class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = 'name'

    es_socio = fields.Boolean(string='Es Socio', default=False)
    es_escritor = fields.Boolean(string='Es Escritor', default=False)
    #carnet_id = fields.One2one('bli_carnet', string='Carnet')
