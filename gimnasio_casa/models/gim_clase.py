
from odoo import models, fields

class GimClase(models.Model):
    _name = 'gim.clase'
    _description = 'Clase gimnasio'

    nombre = fields.Char(string='Nombre clase')  
    fecha = fields.Datetime(string='Fecha de la clase')

#    instructor_id = fields.Many2one('', string='Mascota')  # Relación Uno a Muchos
 #   socio_gimnasio_ids = fields.Many2many('res.partner', 'gim_clase_socios_rel', string='clase favorita')  # Relación Muchos a Muchos
