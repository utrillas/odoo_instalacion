# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'instalacion.material'
     _description = 'Stock en almacen'

     name = fields.Char(string='codigo ', required=True)
     description = fields.Text(string= 'descripcion', required=True)
     quantity = fields.Integer(string='cantidad')
     metric_unit = fields.Selection([
          ('unidades','unidades'),
          ('metros','metros'),
          ('kilos','kilos')
     ], default='Seleccione las unidades')
     reserved_quantity = fields.Integer(string='cantidad reservada')

     

     _sql_constraints = [
          ('unique_product_code','unique(name)','El código ya existe')
     ]

     #restriccion de usuarios a la creación de materiales   
    