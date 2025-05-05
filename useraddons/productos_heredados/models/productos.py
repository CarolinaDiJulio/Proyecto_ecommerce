from odoo import api, models, fields

class Productos(models.Model):
    _inherit = ['product.template']

    tipo = fields.Selection(
        selection=[ ('placa', 'Placa'),('equipo', 'Equipo'),('auxiliar', 'Auxiliar'),('componente', 'Componente'),('material', 'Material')],
        string='Tipo de Producto',required=True
    )

    subtipo = fields.Selection(
        selection=[ ('shd', 'SHD'),('tht', 'THT'),],
        string='Subtipo de Componente', 
    )
    fabricante = fields.Char(string='Fabricante')
    id_fabricante = fields.Char(string='ID Fabricante')
    proveedor = fields.Char(string='Proveedor')

    @api.onchange('tipo')
    def _onchange_tipo(self):
        if self.tipo != 'componente':
            self.subtipo = False