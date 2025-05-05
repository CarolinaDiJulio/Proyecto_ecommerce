from odoo import api, models, fields

class MiProyectoTarea(models.Model):
    _name = 'proyecto.tareas'
    _description = 'Tarea de Proyecto'

    orden_fabricacion = fields.Char(string='Nombre de la Tarea', required=True)
    cantidad = fields.Integer(string='Cantidad', required=True)
    proyecto_id = fields.Many2one('mi.proyecto', string='Proyecto')
    etapa_id = fields.Many2one('proyecto.etapas', string='Etapa', required=True, group_expand='_expand_etapas')
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
        ('3', 'Urgente'),
    ], string='Prioridad', default='1')
    fecha_final = fields.Date(string='Fecha Final')
    inspeccion_visual = fields.Boolean(string='Inspección Visual')
    pruebas = fields.Boolean(string='Pruebas')
    lista = fields.Text(string='Lista de Verificación')
    observaciones = fields.Text(string='Observaciones', default='Sin observaciones...')

    @api.model
    def _expand_etapas(self,domain, order):
        return self.env['proyecto.etapas'].search([], order='sequence') 