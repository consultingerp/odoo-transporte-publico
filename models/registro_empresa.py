# -*- coding: utf-8 -*-
from openerp import api, fields, models

class registro_empresa(models.Model):
    _name = 'registro.empresa'
    _rec_name = 'name'
    name = fields.Char('Nombre Empresa', size=100, required=True)