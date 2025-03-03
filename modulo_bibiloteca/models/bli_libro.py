from odoo import models, fields

#estructura de datos oara uno a muchos
class BibliotecaLibro(models.Model):
    _name = 'bli.libro'
    _description = 'Libro de la biblioteca'

    isbn = fields.Text(string='ISBN cod')
    title = fields.Text(string='Tiulo del libro')
    #autor_id = fields.Many2one('res.partner', string = 'Autor')
    #prestamo_id = fields.One2many('bli.prestamo', 'prestamo_id', string = 'Prestamo')
    #socio_fav_ids = fields.Many2many('res.partner', 'bli_libro_sociofav_rel', string='Favorito del socio')

