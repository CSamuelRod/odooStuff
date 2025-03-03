from odoo import models, fields

#estructura de datos oara uno a muchos
class BibliotecaCarnet(models.Model):
    _name = 'bli.carnet'
    _description = 'Carnet de socio'
    
    numero_carnet = fields.Text(string='Numero de carnet')
    nombre_socio = fields.Text(string='Nombre del socio')
    #socio_id = fields.One2one('res_partner', string = 'Socio titular')

