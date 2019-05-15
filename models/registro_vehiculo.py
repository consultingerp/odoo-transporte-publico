# -*- coding: utf-8 -*-
from openerp import api, fields, models
from . import registro_marca

class registro_vehiculo(models.Model):
    _name = 'registro.vehiculo'
    _rec_name = 'name'
    vehiculo_id = fields.Integer('ID', required=True)
    name = fields.Char('Lateral', size=100, required=True)
    marca = fields.Many2one('registro.marca', 'Marca', select=True, track_visibility='onchange')
    placa = fields.Char('Placa', required=True)
    modelo = fields.Integer('Modelo', required=True)
    cilindrada = fields.Float('Cilindrada', required=True)
    capacidad = fields.Integer('Capacidad', required=True)
    foto_vehiculo = fields.Binary('Foto')
    _sql_constraints = [('name_uniq', 'unique(name)', 'El lateral del vehículo debe ser único.'),
                        ('placa_uniq', 'unique(placa)', 'El número de placa debe ser único.')]