# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
     _name = 'instalacion.employee'
     _description = 'employees of the company'

     #datos principales de los trabajadores
     name = fields.Integer(string='Numero empleado')
     employee_name = fields.Char(string='Nombre completo')
     email = fields.Char('Correo electronico')
     studies = fields.Text('Estudios')
     employee_address = fields.Text('Direccion')
     personal_phone = fields.Char('Telefono personal')
     company_phone = fields.Char('Telefono empresa')
     position = fields.Selection([
          ('directorRegional','Director regional'),
          ('responsable_instalaciones','Responsable Instalaciones'),
          ('project_manager','Project Manager'),
          ('coordinador','Coordinador'),
          ('tecnico_documentacion','Tecnico documentacion'),
          ('secretaria','Secretaria'),
          ('tecnico_de_instalaciones', 'tecnico de instalaciones')
          ],required=True, default='Seleccione un cargo')
     preventive_resource = fields.Boolean(
          string='Recurso preventivo',
          store=True)
     

     #restricciones
     _sql_constraints = [
          ('unique_name','unique(name)','El numero de empleado ya esta usado'),
          ('unique_email','unique(email)','El email ya esta siendo por otro empleado'),
          ('unique_company_phone','unique(company_phone)','El numero de telefono ya esta siendo utilizado por otro empleado') 
     ]

     #relaciones con las tablas
     employee_work_order_id = fields.Many2one('instalacion.work_order')
     
     #crea un codigo de empleado
     """def create(self, vals):
          vals['name'] = self.env['ir.sequence'].next_by_code('secuencia_empleado')
          return super(Employee, self).create(vals) """
     """ def create(self, vals):
          if isinstance(vals, list):
               vals = vals[0]  # Si vals es una lista, toma el primer elemento como diccionario
               vals['name'] = self.env['ir.sequence'].next_by_code('secuencia_empleado')
               return super(Employee, self).create(vals) """
