# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'instalacion.material'
     _description = 'Stock en almacen'

     name = fields.Char(string='codigo ', readonly=1)
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

        
     @api.model
     def create(self, vals):
          vals['name'] = self.env['ir.sequence'].next_by_code('secuencia_material')
          return super(Material,self).create(vals)