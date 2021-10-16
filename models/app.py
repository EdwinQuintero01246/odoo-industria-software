# -*- coding: utf-8 -*-

from odoo import models, fields, api


class app(models.Model):
    _name = 'mimodulo.app'
    _description = 'app'

    name = fields.Char(string='Nombre', required=True)
    versions = fields.Text(string='Versión')
    installs = fields.Boolean(string='Instalado')
    precio = fields.Float(string='Precio')
    fecha = fields.Date(string='fecha instalación')

    @api.onchange('installs')
    def onchange_installs(self):
        print('11111111')
        if self.installs:
            self.precio = 50.00
        else:
            self.precio = 0.00

    