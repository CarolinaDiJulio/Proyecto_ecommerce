from odoo import api, models, fields
from odoo.exceptions import UserError

class Clientes(models.Model):
    _name = 'clientes'
    _description = 'Clientes'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    email = fields.Char(string='Email', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    direccion = fields.Text(string='Dirección')
    ciudad = fields.Char(string='Ciudad')
    pais = fields.Char(string='País')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')