from odoo import models, fields

class BiblioCasaPrestamo(models.Model):
    _name = 'biblio_casa.prestamo'
    _description = 'Prestamo de libro'

    fecha_prestamo = fields.Datetime(string='Fecha de prestamo')
    fecha_devolucion = fields.Datetime(string='Fecha de devolución')
    #libro_id = fields.Many2one('biblio_casa.libro', string='Libro prestado')
    #socio_id = fields.Many2one('res.partner', string='Socio')