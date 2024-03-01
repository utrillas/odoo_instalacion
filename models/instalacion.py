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
     fase = fields.Selection([('ENT', 'Nueva OT'), ('REP', 'Replanteo'), ('PREP', 'Preparacion'), ('OBRA', 'Obra'), ('FIN', 'Fin Obra')], required=True, default='ENT')
     material = fields.Selection([('ENT', 'Sin material'), ('MAT_MAT', 'Material privado'), ('MAT_ESP', 'Matereial especial'), ('MAT_EXT', 'Material extra'), ('MAT_COM', 'Material completado')], required= True, default='ENT')
     
     #obra
     

     _sql_constraints = [
          ('unique_name','unique(name)','El site ya esta registrado')
     ]

     #fases de obra
     def funcion_replanteo(self):
          if self.fase == 'ENT':
               if self.work_order_ids.name != False: 
                    self.write({'fase':'REP'})
          elif self.fase == 'REP':
               if self.work_order_ids.approved_staking_out == True:
                    print(self.work_order_ids.approved_staking_out)
                    self.write({'fase':'PREP'})
               else:
                    raise ValueError('No se ha aprobado el replanteo aún.')
          elif self.fase == 'PREP':
               if self.material == 'MAT_COM':
                    self.write({'fase':'OBRA'})
               else: 
                    raise ValueError('No esta todo el material, compruebe que esta todo.')
          
               
               
                    

               

     
