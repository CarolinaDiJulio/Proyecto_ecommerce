from odoo import api, models, fields

class MiProyecto(models.Model):
    _name= 'mi.proyecto'
    _description = 'Mi Proyecto'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción') 
    tarea_ids = fields.One2many('proyecto.tareas', 'proyecto_id', string='Tareas')
    etapa_ids = fields.One2many('proyecto.etapas', 'proyecto_id', string='Etapas')
    tarea_contador = fields.Integer(string="Cantidad de Tareas", compute='_compute_tarea_contador')

    def _compute_tarea_contador(self):
        for record in self:
            record.tarea_contador = len(record.tarea_ids)