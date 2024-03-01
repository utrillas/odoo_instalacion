# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons import mail


class WorkOrderMaterialRel(models.Model):
     _name = 'instalacion.work_order_material_rel'
     _description = 'material extra para la orden de trabajo'

     #datos especificos de extra_material_rel
     name= fields.Char(string='orden de reserva', required=True)
     needed_material= fields.Float(string='cantidad de material necesario')
     #relacion entre las tablas work_order y material
     material_id = fields.Many2one('instalacion.material')# codigo del material que queremos coger del stock
     work_order_id = fields.Many2one('instalacion.work_order')#PI del site
     material_name = fields.Char(related='material_id.name')

     _sql_constraints = [
          ('unique_material_work_order', 'unique(material_id,work_order_id)','El material no se encuentra')
     ]


     #para actualizar el material que hay en stock despues de reserva.
     @api.onchange('needed_material', 'material_id')
     def _onchange_needed_material(self):
          if self.material_id and self.needed_material:
               self.material_id.quantity -= self.needed_material