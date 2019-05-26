# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registro_conductor(models.Model):
    _name = 'registro.conductor'
    _rec_name = 'name'
    conductor_id = fields.Integer('ID', required=True)
    name = fields.Char('Nombre', size=100, required=True)
    apellido = fields.Char('Apellido', required=True)
    direccion = fields.Char('Dirección', required=True)
    telefono = fields.Integer('Teléfono', required=True)
    identificacion = fields.Integer('Identificación', required=True)
    foto_conductor = fields.Binary('Foto')
    _sql_constraints = [('name_uniq', 'unique(identificacion)', 'El número de identificación debe ser único.'),
                        ('id_uniq', 'unique(conductor_id)', 'El ID debe ser único.')]