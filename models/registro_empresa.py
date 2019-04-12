# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registro_empresa(models.Model):
    _name = 'registro.empresa'
    _rec_name = 'name'
    name = fields.Char('Empresa', size=100, required=True)
    direccion = fields.Char('Dirección', size=100, required=True)
    telefono = fields.Integer('Teléfono', size=100, required=True)
    nit = fields.Char('Nit', size=100, required=True)