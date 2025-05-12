from odoo import api, models, fields

class MiProyectoEtapas(models.Model):
    _name = 'proyecto.etapas'
    _description = 'Etapas del Proyecto' 
    
    name = fields.Char(string='Nombre de la Etapa', required=True)
    proyecto_id = fields.Many2one('mi.proyecto', string='Proyecto')
    sequence = fields.Integer(string='Orden',default=0)
    fold = fields.Boolean(string='Colapsar en Kanban', default=False)  

    _sql_constraints = [
        ('unico_orden_por_proyecto',  
         'UNIQUE(proyecto_id, sequence)', 
         'No puede haber dos etapas con el mismo orden en el mismo proyecto.')
    ]

    @api.model
    def _get_default_proyecto(self):
        proyecto_id = self.env.context.get('active_id')
        if proyecto_id:
            return proyecto_id
        return False
   
    