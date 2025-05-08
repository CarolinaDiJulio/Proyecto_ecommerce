from datetime import timedelta
from odoo import api, models, fields

class MiProyectoTarea(models.Model):
    _name = 'proyecto.tareas'
    _description = 'Tarea de Proyecto'

    # Campos
    orden_fabricacion = fields.Many2one(
        'mrp.production', 
        string='Orden de Fabricación', 
        required=True,
    )
    cantidad = fields.Integer(string='Cantidad', compute='_compute_orden_data')
    proyecto_id = fields.Many2one('mi.proyecto', string='Proyecto')
    etapa_id = fields.Many2one('proyecto.etapas', string='Etapa', required=True, group_expand='_expandir_etapas')
    prioridad = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
        ('3', 'Urgente'),
    ], string='Prioridad',compute='_compute_prioridad')
    fecha_final = fields.Date(string='Fecha Final', required=True, compute='_compute_orden_data')
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
    ultima_etapa = fields.Boolean(string='¿Última Etapa?', compute='_compute_es_ultima_etapa')
    primera_etapa = fields.Boolean(string='¿Primera Etapa?', compute='_compute_es_primera_etapa')

    #sql_constraints para evitar duplicados
    _sql_constraints = [
        ('unique_orden_fabricacion_per_proyecto', 
         'UNIQUE(proyecto_id, orden_fabricacion)',
         'No puede haber dos tareas con el mismo "Orden de Fabricación" en el mismo proyecto.') 
    ] 
    
    # api.depends, campos computados
    @api.depends('etapa_id', 'proyecto_id')
    def _compute_es_ultima_etapa(self):
        for record in self:
            record.ultima_etapa = False
            if record.etapa_id and record.proyecto_id:
                etapas = self._obtener_etapas_ordenadas(record.proyecto_id.id)
                if etapas and record.etapa_id.id == etapas[-1].id:
                    record.ultima_etapa = True

    @api.depends('etapa_id', 'proyecto_id')
    def _compute_es_primera_etapa(self):
        for record in self:
            record.primera_etapa = False
            if record.etapa_id and record.proyecto_id:
                etapas = self._obtener_etapas_ordenadas(record.proyecto_id.id)
                if etapas and record.etapa_id.id == etapas[0].id:
                    record.primera_etapa = True
                    
    @api.depends('orden_fabricacion.product_qty', 'orden_fabricacion.date_finished')
    def _compute_orden_data(self):
        for record in self:
            record.cantidad = record.orden_fabricacion.product_qty or 0
            record.fecha_final = record.orden_fabricacion.date_finished or fields.Date.today()

    @api.depends('fecha_final')
    def _compute_prioridad(self):
        for record in self:
            if record.fecha_final:
                hoy = fields.Date.today()
                if record.fecha_final < hoy + timedelta(days=5):
                    record.prioridad = '3'  # Urgente
                elif record.fecha_final < hoy + timedelta(days=10):
                    record.prioridad = '2'  # Alta
                elif record.fecha_final < hoy + timedelta(days=15):
                    record.prioridad = '1'  # Media
                else:
                    record.prioridad = '0'  # Baja
            else:
                record.prioridad = '0'

    @api.depends('proyecto_id')
    def _compute_ordenes_fabricacion(self):
        for tarea in self:
            if tarea.proyecto_id:
                productos = self.env['product.product'].search([ ('tipo', 'ilike', tarea.proyecto_id.name) ])
                ordenes = self.env['mrp.production'].search([ ('product_id', 'in', productos.ids) ])
                tarea.ordenes_fabricacion_ids = ordenes
            else:
                tarea.ordenes_fabricacion_ids = False
    
    # api.models
    @api.model
    def _get_default_proyecto(self):
        proyecto_id = self.env.context.get('active_id')
        if proyecto_id:
            return proyecto_id
        return False
    
    @api.model
    def _expandir_etapas(self,domain=None, order='sequence'):
        proyecto_id = self.env.context.get('active_id')
        if proyecto_id: 
            return self._obtener_etapas_ordenadas(proyecto_id)
        return self._obtener_etapas_ordenadas()
    
    # Funciones
    def action_mover_etapa_anterior(self):
        if self.etapa_id and self.proyecto_id:
            etapas_ordenadas = self._obtener_etapas_ordenadas(self.proyecto_id.id)
            etapa_anterior = etapas_ordenadas.filtered(lambda e: e.sequence < self.etapa_id.sequence)
            if etapa_anterior:
                self.etapa_id = etapa_anterior[-1]

    def action_mover_etapa_siguiente(self):
        if self.etapa_id and self.proyecto_id:
            etapas_ordenadas = self._obtener_etapas_ordenadas(self.proyecto_id.id)
            siguiente_etapa = etapas_ordenadas.filtered(lambda e: e.sequence > self.etapa_id.sequence)
            if siguiente_etapa:
                self.etapa_id = siguiente_etapa[0]

    def _obtener_etapas_ordenadas(self, proyecto_id=None):
        proyecto_id = proyecto_id or self.env.context.get('active_id')
        if proyecto_id:
            return self.env['proyecto.etapas'].search([('proyecto_id', '=', proyecto_id)], order='sequence')
        return self.env['proyecto.etapas'].search([], order='sequence')

    def action_ultima_etapa(self):
        for record in self:
            record.unlink()