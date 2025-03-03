from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_socio_casa = fields.Boolean(string='Es Socio', default=False)
    es_escritor_casa = fields.Boolean(string='Es Escritor', default=False)
    carnet_id = fields.One2many('biblio_casa.carnet','socio_id', string='Carnet')
    prestamo_ids = fields.One2many('biblio_casa.prestamo', 'socio_id', string='Prestamos')
    libro_fav_ids = fields.Many2many('biblio_casa.libro', 'biblio_casa_libro_sociofav_rel', string='Libros Favoritos')
    libro_ids = fields.One2many('biblio_casa.libro', 'autor_id', string='Libros Escritos')