# -*- coding: utf-8 -*-
from openerp import api, fields, models
from . import registro_marca

class registro_vehiculo(models.Model):
    _name = 'registro.vehiculo'
    _rec_name = 'name'
    vehiculo_id = fields.Integer('ID', required=True)
    name = fields.Char('Lateral', size=100, required=True)
    marca = fields.Many2one('registro.marca', 'Marca', select=True, track_visibility='onchange', required=True)
    placa = fields.Char('Placa', required=True)
    modelo = fields.Integer('Modelo', required=True)
    cilindrada = fields.Float('Cilindrada', required=True)
    capacidad = fields.Integer('Capacidad', required=True)