# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstallationsOffice(models.Model):
     _name = 'instalacion.installations_office'
     _description = 'Employees of the facilities office'

     _inherit = 'instalacion.employee'

     #dato especifico de los trabajadores de la oficina de instalaciones
     name = fields.Selection([
          ('director regional','Director regional'),
          ('responsable Instalaciones','Responsable Instalaciones'),
          ('project Manager','Project Manager'),
          ('coordinador','Coordinador'),
          ('tecnido documentacion','Tecnico documentacion'),
          ('secretaria','Secretaria')
          ],required=True, default='Seleccione un cargo')
