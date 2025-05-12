from odoo import api, models, fields
from odoo.exceptions import UserError

class Categorias(models.Model):
    _name= 'categorias'
    _description = 'categorias'

    name = fields.Char(string="Nombre categoría...")