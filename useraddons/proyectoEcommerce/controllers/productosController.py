from odoo.http import request

from odoo import http

class MiTienda(http.Controller):
    @http.route('/mitienda/productos', auth='public', website=True)
    def productos(self, **kwargs):
        # Obtén los productos de tu modelo 'productos'
        productos = http.request.env['productos'].search([])
        
         # Verificar si hay productos disponibles
        if not productos:
            return http.request.render('proyectoEcommerce.no_productos_template')  # Plantilla para cuando no haya productos
        
        return http.request.render('proyectoEcommerce.productosqweb_views', {
            'productos': productos
        })
    
    @http.route('/mitienda/producto/<int:producto_id>', auth='public', website=True)
    def producto_detalle(self, producto_id):
        producto = request.env['productos'].sudo().browse(producto_id)
        if not producto.exists():
            return request.not_found()
        return request.render('proyectoEcommerce.producto_detalle_template', {
            'producto': producto,
        }) 
