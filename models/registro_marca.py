# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registro_marca(models.Model):
    _name = 'registro.marca'
    _rec_name = 'name'
    name = fields.Char('Nombre', size=100, required=True)