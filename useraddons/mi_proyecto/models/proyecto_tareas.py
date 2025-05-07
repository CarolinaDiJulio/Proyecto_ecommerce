from datetime import timedelta
from odoo import api, models, fields

class MiProyectoTarea(models.Model):
    _name = 'proyecto.tareas'
    _description = 'Tarea de Proyecto'

    #orden_fabricacion = fields.Char(string='Nombre de la Tarea', required=True)
    orden_fabricacion = fields.Many2one(
        'mrp.production', 
        string='Orden de Fabricación', 
        required=True,
    )
    cantidad = fields.Integer(string='Cantidad')
    proyecto_id = fields.Many2one('mi.proyecto', string='Proyecto')
    etapa_id = fields.Many2one('proyecto.etapas', string='Etapa', required=True, group_expand='_expandir_etapas')
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
        ('3', 'Urgente'),
    ], string='Prioridad')
    fecha_final = fields.Date(string='Fecha Final', required=True, default=fields.Date.today())
    inspeccion_visual = fields.Boolean(string='Inspección Visual')
    pruebas = fields.Boolean(string='Pruebas')
    lista = fields.Text(string='Lista de Verificación')
    observaciones = fields.Text(string='Observaciones')

    # Campo auxiliar 
    ordenes_fabricacion_ids = fields.Many2many(
        'mrp.production', 
        compute='_compute_ordenes_fabricacion', 
        store=False
    )

    _sql_constraints = [
        ('unique_orden_fabricacion_per_proyecto', 
         'UNIQUE(proyecto_id, orden_fabricacion)',
         'No puede haber dos tareas con el mismo "Orden de Fabricación" en el mismo proyecto.') 
    ] 

    # @api.onchange('proyecto_id')
    # def onchange_proyecto_id(self):
    #     # Actualizar las etapas disponibles según el proyecto seleccionado
    #     if self.proyecto_id:
    #         return {
    #             'domain': {'etapa_id': [('proyecto_id', '=', self.proyecto_id.id)]}
    #         }
    #     else:
    #         return {
    #             'domain': {'etapa_id': []}
    #         }

    @api.onchange('orden_fabricacion')
    def _onchange_orden_fabricacion(self):
        if self.orden_fabricacion:
            self.cantidad = self.orden_fabricacion.product_qty

            # Asignar fecha final si está disponible
            if self.orden_fabricacion.date_finished:
                self.fecha_final = fields.Date.to_date(self.orden_fabricacion.date_finished)
            else:
                self.fecha_final = fields.Date.today()
        else:
            self.cantidad = 0
            self.fecha_final = fields.Date.today()

    
    @api.onchange('fecha_final')
    def _onchange_fecha_final(self):
        if self.fecha_final:
            # Validar que la fecha final no sea anterior a la fecha actual
            if self.fecha_final < fields.Date.today()+ timedelta(days=5):
                self.prioridad = '3'  # Urgente
            elif self.fecha_final < fields.Date.today() + timedelta(days=10):
                self.prioridad = '2'  # Alta
            elif self.fecha_final < fields.Date.today() + timedelta(days=15):
                self.prioridad = '1'  # Media
            else:
                self.prioridad = '0'  # Baja

    @api.depends('proyecto_id')
    def _compute_ordenes_fabricacion(self):
        for tarea in self:
            if tarea.proyecto_id:
                productos = self.env['product.product'].search([ ('tipo', 'ilike', tarea.proyecto_id.name) ])
                ordenes = self.env['mrp.production'].search([ ('product_id', 'in', productos.ids) ])
                tarea.ordenes_fabricacion_ids = ordenes
            else:
                tarea.ordenes_fabricacion_ids = False
    
    @api.model
    def _get_default_proyecto(self):
        # Obtener el ID del proyecto desde el contexto activo (si está presente)
        proyecto_id = self.env.context.get('active_id')
        if proyecto_id:
            return proyecto_id
        return False
    
    @api.model
    def _expandir_etapas(self,domain, order):
        proyecto_id = self.env.context.get('active_id')
        if proyecto_id:
            # Filtrar las etapas según el proyecto activo
            return self.env['proyecto.etapas'].search([('proyecto_id', '=', proyecto_id)], order='sequence')
        else:
            # Si no hay un proyecto activo, retornar todas las etapas
            return self.env['proyecto.etapas'].search([], order='sequence')
        # return self.env['proyecto.etapas'].search([], order='sequence') 
    
    def action_mover_etapa_anterior(self):
        if self.etapa_id and self.proyecto_id:
            etapas_ordenadas = self.env['proyecto.etapas'].search(
                [('proyecto_id', '=', self.proyecto_id.id)],
                order='sequence'
            )
            etapa_anterior = etapas_ordenadas.filtered(lambda e: e.sequence < self.etapa_id.sequence)
            if etapa_anterior:
                self.etapa_id = etapa_anterior[-1]

    def action_mover_etapa_siguiente(self):
        if self.etapa_id and self.proyecto_id:
            etapas_ordenadas = self.env['proyecto.etapas'].search(
                [('proyecto_id', '=', self.proyecto_id.id)],
                order='sequence'
            )
            siguiente_etapa = etapas_ordenadas.filtered(lambda e: e.sequence > self.etapa_id.sequence)
            if siguiente_etapa:
                self.etapa_id = siguiente_etapa[0]

