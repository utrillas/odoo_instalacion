# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Instalacion(models.Model):
     _name = 'instalacion.instalacion'
     _description = 'module designed for the management of work carried out in the installation paste of mobile telephony companies.'

     #datos generales
     name = fields.Char(string='Site', required = True, size=8)
     owner = fields.Char()
     address = fields.Text('Direccion')
     population = fields.Char('Poblacion', size=100)
     coordinates = fields.Char('Coordenadas', size=50)
     remarks = fields.Text('Observaciones')
     technical_staking_out = fields.One2many(string='Tecnico replanteo', related='work_order_ids')
     #relaciones con las tablas 
     work_order_ids = fields.One2many('instalacion.work_order', 'instalacion_id', 'Orden de trabajo')
     
     
     _sql_constraints = [
          ('unique_name','unique(name)','El site ya esta registrado')
     ]

     
     
