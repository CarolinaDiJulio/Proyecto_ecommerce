from odoo import api, models, fields
from odoo.exceptions import UserError

class Productos(models.Model):
    _name= 'productos'
    _description = 'Productos'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio', required=True)
    stock = fields.Integer(string='Stock', required=True)
    categoria = fields.Char(string='Categoría', required=True)
    imagen = fields.Binary(string='Imagen')