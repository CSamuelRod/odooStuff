{
    'name': 'Biblioteca',
    'version': '1.0.0',
    'author': 'Rafael Sánchez',
    'category': 'Biblioteca',
    'license': 'LGPL-3',
    'summary': 'Un módulo que administra una biblioteca con libros y autores.',
    'description': """
        Este es un módulo una una biblioteca con libros y autores.
    """,
    'depends': ['base', 'contacts'],  # 'contacts' asegura que 'res.partner' esté disponible
    'data': [
        'security/ir.model.access.csv',
        'views/bli_carnet_views.xml',  # Asegúrate de incluir este archivo
        'views/res_partner_bli_views.xml',  # Asegúrate de incluir este archivo
        'views/bli_libro_views.xml',  
        'views/bli_prestamo_views.xml',
        'views/bli_menus.xml',  # Asegúrate de incluir este archivo

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
