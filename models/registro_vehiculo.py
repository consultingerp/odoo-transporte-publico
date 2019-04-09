# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registrotransportepublico_vehiculo(models.Model):
    _name = 'registrotransportepublico.vehiculo'
    _rec_name = 'name'
    name = fields.Char('Registro Vehículos', size=100, required=True)