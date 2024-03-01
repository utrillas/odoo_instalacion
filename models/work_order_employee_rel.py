# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WorkOrderEmployeeRel(models.Model):
     _name = 'instalacion.work_order_employee_rel'
     _description = 'table showing the technicians to carry out the work orders and stakeouts'



     #busqueda de los tecnicos
     @api.model
     def _default_employee_technical(self):
          return self.env['instalacion.employee'].search([('position', '=', 'tecnico_de_intalaciones')])
     
     #relacion con las tablas
     technical_id = fields.Many2one('instalacion.employee', string='Tecnico replanteo', domain="[('id', 'in', _default_employee_technical)]")
     work_order_technical_id = fields.Many2one('instalacion.work_order')
     preventive_resource = fields.Boolean(
          string='Recurso preventivo')
     
     