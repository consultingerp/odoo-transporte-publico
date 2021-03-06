# -*- coding: utf-8 -*-
from openerp import api, fields, models
from . import registro_conductor, registro_vehiculo

class registro_empresa(models.Model):
    _name = 'registro.empresa'
    _rec_name = 'name'
    name = fields.Char('Empresa', size=100, required=True)
    direccion = fields.Char('Dirección', size=100, required=True)
    telefono = fields.Integer('Teléfono', size=50, required=True)
    nit = fields.Char('Nit', size=50, required=True)
    conductor_id = fields.One2many('registro.conductor', 'conductor_id', 'Conductores', track_visibility='onchange')
    vehiculo_id = fields.One2many('registro.vehiculo', 'vehiculo_id', 'Vehículos', track_visibility='onchange')
    _sql_constraints = [('name_uniq', 'unique(name)', 'Esta empresa ya se encuentra registrada.')]