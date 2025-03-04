{
    'name': 'Gestor gimnasio',
    'version': '1.0.0',
    'author': 'Samuel Rodriguez',
    'category': 'Gimnasio',
    'license': 'LGPL-3',
    'summary': 'Un módulo que reservas de clases de un gimnasio.',
    'description': """
        Módulo para la gestión de clases , profesores y socios.
    """,
    'depends': ['base', 'contacts'],  # 'contacts' asegura que 'res.partner' esté disponible
    'data': [
        'security/ir.model.access.csv',
        'views/gim_membresia_views.xml', 
        'views/gim_reserva.xml', 
        'views/gim_clase_views.xml', 
        'views/res_partner_gim_views.xml',
        'views/gim_menus.xml' 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
