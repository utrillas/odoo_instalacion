# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
     _name = 'instalacion.employee'
     _description = 'employees of the company'

     #datos principales de los trabajadores
     name = fields.Integer(string='Numero empleado', required = True)
     firstname = fields.Char(string='Apellidos')
     employee_name = fields.Char(string='Nombre')
     email = fields.Char('Correo electronico')
     studies = fields.Text('Estudios')
     employee_address = fields.Text('Direccion')
     personal_phone = fields.Char('Telefono personal')
     company_phone = fields.Char('Telefono empresa')
     position = fields.Selection([
          ('director regional','Director regional'),
          ('responsable Instalaciones','Responsable Instalaciones'),
          ('project Manager','Project Manager'),
          ('coordinador','Coordinador'),
          ('tecnido documentacion','Tecnico documentacion'),
          ('secretaria','Secretaria'),
          ('tecnico de instalaciones', 'tecnico de instalaciones')
          ],required=True, default='Seleccione un cargo')
     

     #restricciones
     _sql_constraints = [
          ('unique_name','unique(name)','El numero de empleado ya esta usado'),
          ('unique_email','unique(email)','El email ya esta siendo por otro empleado'),
          ('unique_company_phone','unique(company_phone)','El numero de telefono ya esta siendo utilizado por otro empleado') 
     ]


     