# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.addons import mail


class WorkOrder(models.Model):
     _name = 'instalacion.work_order'
     _description = 'Work order of a site'

     #datos generales de la orden de trabajo
     name = fields.Char(string='PI', required = True) 
     date_creation = fields.Date(string= 'Fecha creación', default=lambda self: fields.Date.today())
     date_staking_out = fields.Date(string='Fecha replanteo')
     date_work = fields.Date(string='Fecha Obra')
     date_end = fields.Date(string='Fecha fin')

     #replanteo
     reusable_material = fields.Boolean(string="Material reutilizable", default=False)
     reusable = fields.Text(string="Descripcion del material reutilizable")
     staking_out_data = fields.Text(string="Descripción del replanteo")
     approved_staking_out = fields.Boolean('Aprobado replanteo', widget='binary')
     rejected_staking_out = fields.Boolean('Rechazado replanteo', widget='binary')


     #relaciones con las tablas 
     need_material_ids = fields.Many2many('instalacion.material', string='Material extra')
     #instalacion_id = fields.Many2one('instalacion.instalacion', 'Nueva orden de trabajo en Site')
     stakeout_technician_ids = fields.Many2many('instalacion.technical', string='Tecnico replanteo')

     #restricciones
     _sql_constraints = [
          ('unique_name','unique(name)','La PI ya existe')
     ]
"""
     #funcion para que me enseñe el texto de material reutilizables
     ##############NO FUNCIONA CUANDO CAMBIE LAS VISTAS, PREGUNTAR POR QUE NO FUNCIONA##########
     @api.onchange('reusable_material')
     def _onchange_reusable_material(self):
          if not self.reusable_material:
               self.reusable = False

     #función para que avise si no hay suficiente cantidad y que la reste si hay suficiente
     ######## NO FUNCIONA LA PARTE DE RESTA PREGUNTAR A ALFREDO########
     @api.onchange('need_quantity')
     def reserve_material(self):
          for rec in self:
               for material in rec.need_material:
                    if rec.need_quantity > material.quantity:
                         raise UserError('No hay suficinete cantidad disponible, por favor, hacer compra.')
                    else:
                         material.write({'producto.quantity': material.quantity - rec.need_quantity})

     #funcion para que los datos del replanteo sean editables
     @api.onchange('date_staking_out')
     def onchange_date_staking_out(self):
          for rec in self:
               if rec.date_staking_out:
                    rec.update({
                         'date_staking_out':False
                    })
               else:
                    rec.update({
                         'date_staking_out': True
                    })
"""