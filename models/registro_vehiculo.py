# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registro_vehiculo(models.Model):
    _name = 'registro.vehiculo'
    _rec_name = 'name'
    name = fields.Char('Marca', size=100, required=True)
    placa = fields.Char('Placa', required=True)