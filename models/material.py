# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'instalacion.material'
     _description = 'Stock en almacen'
     _rec_name = 'description'

     name = fields.Char(string='codigo ', readonly=1)
     description = fields.Text(string= 'descripcion', required=True)
     quantity = fields.Float(string='cantidad en Stock')
     metric_unit = fields.Selection([
          ('unidades','unidades'),
          ('metros','metros'),
          ('kilos','kilos')
     ], default='Seleccione las unidades')

     

     _sql_constraints = [
          ('unique_name','unique(name)','El código ya existe')
     ]

     stock_ids = fields.One2many('instalacion.reserve_line', 'material_id',  string='Material existente')
        
     @api.model
     def create(self, vals):
          vals['name'] = self.env['ir.sequence'].next_by_code('secuencia_material')
          return super(Material,self).create(vals)
     