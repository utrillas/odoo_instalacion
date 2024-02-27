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
     
     #relaciones con las tablas 
     work_order_ids = fields.One2many('instalacion.work_order', 'name', 'Orden de trabajo')
     empleados_technical_ids = fields.Many2many('instalacion.technical')
     empleados_of_installations_ids= fields.Many2many('instalacion.of_installations')
     
     
     _sql_constraints = [
          ('unique_name','unique(name)','El site ya esta registrado')
     ]

     
     
