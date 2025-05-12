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
    
    @http.route('/mitienda/productos', auth='public', website=True)
    def productos(self, precio=None, categoria=None):

        categorias = request.env['categorias'].search([])
        
        # Establecer los rangos de precio
        if precio in [None, ""]:
            # Sin filtro de precio, muestra todos los productos
            productos = request.env['productos'].sudo().search([])
        elif precio == '1':
            productos = request.env['productos'].sudo().search([('precio', '<', 20)])
        elif precio == '2':
            productos = request.env['productos'].sudo().search([('precio', '>=', 20), ('precio', '<=', 50)])
        elif precio == '3':
            productos = request.env['productos'].sudo().search([('precio', '>=', 50), ('precio', '<=', 100)])
        elif precio == '4':
            productos = request.env['productos'].sudo().search([('precio', '>', 100)])
        else:
            productos = request.env['productos'].sudo().search([])

        if categoria:
            productos = productos.filtered(lambda p: p.categoria.id == int(categoria))
        # Pasar los productos al template
        return request.render('proyectoEcommerce.productosqweb_views', {
            'productos': productos,
            'categorias': categorias,
        })