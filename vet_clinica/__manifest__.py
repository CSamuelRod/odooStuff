{
    'name': 'Clinica Veterinaria',
    'version': '1.0.0',
    'author': 'Marco Zeta',
    'category': 'Veterinaria',
    'license': 'LGPL-3',
    'summary': 'Un módulo que administra una clinica veterinaria.',
    'description': """
        Módulo para la gestión de mascotas, citas veterinarias y propietarios en Odoo.
    """,
    'depends': ['base', 'contacts'],  # 'contacts' asegura que 'res.partner' esté disponible
    'data': [
        'security/ir.model.access.csv',
        'views/vet_mascota_views.xml',          # Vistas Mascotas
        'views/vet_cita_views.xml',             # Vistas Citas
        'views/res_partner_vet_views.xml',      # res.partner
        'views/vet_menus.xml',                  # Menús del Módul
       # 'views/grades_course_views.xml',  # Asegúrate de incluir este archivo
       # 'views/res_partner_views.xml',  # Asegúrate de incluir este archivo
       # 'views/grades_evaluation_views.xml',  
       # 'views/grades_manager_menus.xml',  # Asegúrate de incluir este archivo

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
