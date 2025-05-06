from odoo import api, models, fields

class MiProyecto(models.Model):
    _name= 'mi.proyecto'
    _description = 'Mi Proyecto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción') 
    tarea_ids = fields.One2many('proyecto.tareas', 'proyecto_id', string='Tareas')
    etapa_ids = fields.One2many('proyecto.etapas', 'proyecto_id', string='Etapas')