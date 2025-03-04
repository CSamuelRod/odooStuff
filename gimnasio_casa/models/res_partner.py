
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_socio_gimnasio = fields.Boolean(string='Es socio del gimnasio', default=False)
    es_instructor = fields.Boolean(string='Es instructor del gimnasio', default=False)

    # membresia_id = fields.One2many('gim.membresia', 'socio_gimnasio_id', string='Membresía')
    # reservas_ids = fields.One2many('gim.reserva', 'socio_id', string='Reservas')