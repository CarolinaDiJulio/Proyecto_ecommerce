from odoo import api, models, fields
from odoo.exceptions import UserError

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

    def write(self, vals):
        if 'name' in vals:
            for record in self:
                if record.name:
                    raise UserError("No se puede cambiar el nombre del proyecto una vez creado.")
        return super(MiProyecto, self).write(vals)