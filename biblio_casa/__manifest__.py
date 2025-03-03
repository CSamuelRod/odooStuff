{
    'name': 'Biblioteca casa',
    'version': '1.0.0',
    'author': 'Samuel Rodriguez',
    'category': 'Biblioteca casa',
    'license': 'LGPL-3',
    'summary': 'Modulo para administrar una biblioteca.',
    'description': """
        Este es un módulo de una biblioteca con libros y autores.
    """,
    'depends': ['base', 'contacts'],  # 'contacts' asegura que 'res.partner' esté disponible
    'data': [
        'security/ir.model.access.csv',
        'views/biblio_casa_carnet_views.xml',  # Asegúrate de incluir este archivo
        'views/res_partner_bli_views.xml',  # Asegúrate de incluir este archivo
        'views/biblio_casa_libro_views.xml',  
        'views/biblio_casa_prestamo_views.xml',
        'views/bli_menus.xml',  # Asegúrate de incluir este archivo

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
