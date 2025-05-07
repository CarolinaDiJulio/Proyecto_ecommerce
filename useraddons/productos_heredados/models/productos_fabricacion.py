from odoo import models, fields 
# Nueva clase que hereda de product.product, en el mismo módulo
class ProductosFabricacion(models.Model):
    _inherit = 'product.product'

    tipo = fields.Selection(
        related='product_tmpl_id.tipo',
        selection=[
            ('placa', 'Placa'),
            ('equipo', 'Equipo'),
            ('auxiliar', 'Auxiliar'),
            ('componente', 'Componente'),
            ('material', 'Material')
        ],
        string='Tipo de Producto',
        store=True,
        readonly=True
    )
    subtipo = fields.Selection(
        related='product_tmpl_id.subtipo',
        selection=[
            ('shd', 'SHD'),
            ('tht', 'THT')
        ],
        string='Subtipo de Componente',
        store=True,
        readonly=True
    )
    fabricante = fields.Char(
        related='product_tmpl_id.fabricante',
        string='Fabricante',
        store=True,
        readonly=True
    )
    id_fabricante = fields.Char(
        related='product_tmpl_id.id_fabricante',
        string='ID Fabricante',
        store=True,
        readonly=True
    )
    proveedor = fields.Char(
        related='product_tmpl_id.proveedor',
        string='Proveedor',
        store=True,
        readonly=True
    )
