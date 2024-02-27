# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons import mail


class ExtraMaterialRel(models.Model):
     _name = 'instalacion.extra_material_rel'
     _description = 'material extra para la orden de trabajo'

     
     name= fields.Char(string='orden de reserva')
     needed_material= fields.Float(string='material necesario')


     material_id = fields.Many2one('instalacion.material')
     work_order_id = fields.Many2one('instalacion.work_order')

     _sql_constraints = [
          ('unique_material_work_order', 'unique(material_id,work_order_id)','El material no se encuentra')
     ]


     #para actualizar el material que hay en stock despues de reserva.
     @api.onchange('needed_material', 'material_id')
     def _onchange_needed_material(self):
          if self.material_id and self.needed_material:
               self.material_id.quantity -= self.needed_material