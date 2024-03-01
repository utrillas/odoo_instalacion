# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
     _name = 'instalacion.material'
     _description = 'Stock en almacen'

     name = fields.Char(string='codigo ')
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

     sock_ids = fields.One2many('instalacion.work_order_material_rel', 'material_id',  string='Material existente')
        
     """ @api.model
     def create(self, vals):
          vals['name'] = self.env['ir.sequence'].next_by_code('secuencia_material')
          return super(Material,self).create(vals) """
     