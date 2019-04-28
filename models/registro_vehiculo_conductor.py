# -*- coding: utf-8 -*-
from openerp import api, fields, models
from . import registro_conductor, registro_vehiculo

class registro_vehiculo_conductor(models.Model):
    _name = 'registro.vehiculo_conductor'
    _rec_name = 'name'

    name = fields.Many2one('registro.empresa', 'Empresa', select=True, track_visibility='onchange)
    conductor_id = fields.Many2one('registro.conductor', 'Conductor', select=True, track_visibility='onchange')
    vehiculo_id = fields.Many2one('registro.vehiculo', 'Vehículo', select=True, track_visibility='onchange')