# -*- coding: utf-8 -*-
{
    'name': 'Productos',
    'version': '1.0',
    'summary': 'Muestra los productos',
    'description': " ",
    'author': 'D2PLUS',
    'website': 'https://www.d2plus.com',  # Opcional
    'category': 'Inventory',
    'sequence': 25,  # Orden en el menú de aplicaciones
    'depends': [
        'base',   # Dependencia principal para usar el modelo base
        'web',    # Dependencia para la interfaz web de Odoo
        'mrp',
    ],
    "data": [
        "views/menus_views.xml",
        "views/mi_proyecto_views.xml",
        "views/proyecto_etapas_views.xml",
        "views/proyecto_tareas_views.xml"
    ],
    'installable': True,     # Habilita la instalación del módulo
    'application': True,     # Especifica que el módulo es una aplicación
    'assets': {
        # Debe ir en 'web.assets_backend' porque la vista kanban se muestra en el backend de Odoo
         'web.assets_backend': [
                'mi_proyecto/static/src/css/style.css', 
                'mi_proyecto/static/src/js/script.js',
            ],
    },
    'license': 'LGPL-3',     # Licencia del módulo, ajusta según sea necesario
}
