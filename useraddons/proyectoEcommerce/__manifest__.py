# -*- coding: utf-8 -*-
{
    'name': 'Proyecto Ecommerce',
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
        'product', # Dependencia para el módulo de productos
        'stock',   # Dependencia para el módulo de inventario
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/menus_views.xml",
        "views/no_productos_template.xml",
        "views/producto_detalle_template.xml",
        "views/productosqweb_views.xml"
    ],
    'installable': True,     # Habilita la instalación del módulo
    'application': True,     # Especifica que el módulo es una aplicación
    'assets': {
        #  'website.assets_frontend': [
        #         'linea/static/src/css/style.css', 
        #     ],
    },
    'license': 'LGPL-3',     # Licencia del módulo, ajusta según sea necesario
}
