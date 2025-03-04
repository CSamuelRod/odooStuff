from odoo import models, fields

class BiblioCasaLibro(models.Model):
    _name = 'biblio_casa.libro'
    _description = 'Libro de la biblioteca'

    isbn = fields.Text(string='ISBN cod')
    title = fields.Text(string='Tiulo del libro')
    #  autor_id = fields.Many2one('res.partner', string='Autor')
    # prestamo_ids = fields.One2many('biblio_casa.prestamo', 'libro_id', string='Prestamo')
    # socio_fav_ids = fields.Many2many('res.partner', 'biblio_casa_libro_sociofav_rel', string='Favorito del socio')