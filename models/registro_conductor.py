# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registro_conductor(models.Model):
    _name = 'registro.conductor'
    _rec_name = 'name'
    name = fields.Char('Nombre', size=100, required=True)
    apellido = fields.Char('Apellido', required=True)
    direccion = fields.Char('Dirección', required=True)
    telefono = fields.Integer('Teléfono', required=True)
    identificacion = fields.Integer('Identificacion', required=True)