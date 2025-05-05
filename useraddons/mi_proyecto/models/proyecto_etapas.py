from odoo import models, fields

class MiProyectoEtapas(models.Model):
    _name = 'proyecto.etapas'
    _description = 'Etapas del Proyecto'

    
    
    name = fields.Char(string='Nombre de la Etapa', required=True)
    proyecto_id = fields.Many2one('mi.proyecto', string='Proyecto')
    sequence = fields.Integer(string='Orden',default=1)
    fold = fields.Boolean(string='Colapsar en Kanban', default=False)