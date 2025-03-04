from odoo import models, fields

class BiblioCasaCarnet(models.Model):
    _name = 'biblio_casa.carnet'
    _description = 'Carnet de socio de biblioteca'

    numero_carnet = fields.Text(string='Numero de carnet')
    nombre_socio = fields.Text(string='Nombre del socio') # Campo agregado
    fecha_vencimiento = fields.Date(string='Fecha de vencimiento')
    #socio_id = fields.Many2one('res.partner', string='Socio titular')