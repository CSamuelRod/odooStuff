from odoo import models, fields

class GimReserva(models.Model):
    _name = 'gim.reserva'
    _description = 'Reserva de clase'

    fecha_reserva = fields.Datetime(string='Fecha de reserva clase')

    # clase_id = fields.Many2one('gim.clase', string='Clase reservada')
    # socio_id = fields.Many2one('res.partner', string='Socio que reserva')
    