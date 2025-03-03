from odoo import models, fields

#estructura de datos oara uno a muchos
class BibliotecaPrestamo(models.Model):
    _name = 'bli.prestamo'
    _description = 'Prestamo de libro'

    fecha_prestamo = fields.Datetime(string='Fecha de prestamo')
    fecha_devolucion = fields.Datetime(string='Fecha de devolución')
    #libro_id = fields.Many2one('bli.libro', string = 'Libro prestado')
    #socio_id = fields.One2many('res.partner', 'socio_id', string = 'Prestamo')
    