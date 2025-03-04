
from odoo import models, fields

class GimMembresia(models.Model):
    _name = 'gim.membresia'
    _description = 'Membresía de socio del gimnasio'

    numero_membresia = fields.Char(string='Número de membresía')  
    nombre_socio = fields.Char(string='Nombre del socio')

    # socio_gimnasio_id = fields.Many2one('res.partner', string='Socio gimnasio')