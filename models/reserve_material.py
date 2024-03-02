# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReserveMaterial(models.Model):
     _name = 'instalacion.reserve_material'
     _description = 'material reservation of a work order'

     #datos especificos:
     name= fields.Char(string='orden de reserva', readonly=1)
     material_name = fields.Text(related='reserve_line_ids.material_name')
     material_quantity = fields.Float(related='reserve_line_ids.needed_material')
     

     #relacion con las tablas
     work_order_id = fields.Many2one('instalacion.work_order')#PI del site
     reserve_line_ids = fields.One2many('instalacion.reserve_line', 'reserve_material_id')

     _sql_constraints = [
          ('unique_name', 'unique(name)','Ya hay un albarán con el mismo número.')
     ]

     @api.model
     def create(self, vals):
          vals['name'] = self.env['ir.sequence'].next_by_code('secuencia_reserva')
          return super(ReserveMaterial, self).create(vals) 