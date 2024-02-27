# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Technical(models.Model):
     _name = 'instalacion.technical'
     _description = 'subgroup of employees, Installation and Maintenance Technicians'

     _inherit = 'instalacion.employee'

     #dato especifico de los tecnicos
     name = fields.Boolean(string='Recurso preventivo', required=True)

