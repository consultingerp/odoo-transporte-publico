# -*- coding: utf-8 -*-
from openerp import api, fields, models
from . import registro_conductor, registro_vehiculo, registro_empresa

class registro_control_salida(models.Model):
    _name = 'registro.control_salida'
    _rec_name = 'name'
    name = fields.Many2one('registro.conductor', 'Conductor', select=True, track_visibility='onchange')
    vehiculo_id = fields.Many2one('registro.vehiculo', 'Vehículo', select=True, track_visibility='onchange')
    empresa_id = fields.Many2one('registro.empresa', 'Empresa', select=True, track_visibility='onchange')
    autorizado = fields.Boolean('¿Salida Autorizada?', default=False, required=True)
    fecha_salida = fields.Datetime('Fecha Salida', default=fields.Date.today, required=True)