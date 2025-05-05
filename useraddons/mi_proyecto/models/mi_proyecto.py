from odoo import api, models, fields

class MiProyecto(models.Model):
    _name= 'mi.proyecto'
    _description = 'Mi Proyecto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')