# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons import mail


class ReserveLine(models.Model):
     _name = 'instalacion.reserve_line'
     _description = 'material extra para la orden de trabajo'

     #datos especificos de extra_material_rel
     name = fields.Integer(string='Numero de linea')
     material_name = fields.Text(related='material_id.description')
     material_code = fields.Char(related='material_id.name')
     needed_material= fields.Float(string='cantidad de material necesario')
     material_quantity = fields.Float(related='material_id.quantity')
     


     #relacion entre las tablas work_order y material
     material_id = fields.Many2one('instalacion.material')# codigo del material que queremos coger del stock
     reserve_material_id = fields.Many2one('instalacion.reserve_material')


     #para actualizar el material que hay en stock despues de reserva.
     @api.onchange('needed_material', 'material_id')
     def _onchange_needed_material(self):
          if self.material_id and self.needed_material:
               self.material_id.quantity -= self.needed_material