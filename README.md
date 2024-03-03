# carmenug.Odoo.Instalaciones.io

URL del repositorio

https://github.com/utrillas/odoo_instalacion

## Proceso de instalación:

Mi módulo de instalaciones de telecomunicaciones no tiene dependencia con ningún módulo.

### Esquema de dependencias:

* base

### Orden del proceso:

1.- **Accede al servidor web donde tienes instalado OdooDock:**
  Necesitas entrar en la máquina o servidor donde está alojando OdooDock. Si estas utilizando Docker, puedes   acceder al contenedor donde se ejecuta OdooDock utilizando el comando:
  
      'docker exec -it [nombre_del_contenedor] bash'
      
2.- **Navega hasta la carpeta extra-addons:**
  Una vez dentro del contenedor, necesitas moverte al directorio donde se almacenan los módulos adiconales     de Odoo. Este directorio se llama **'extra-addons'**. Puedes hacerlo usando el comando:
  
      'cd mnt/extra-addons'
      
3.- **Clona el repositorio que contiene el módulo instalaciones:**
  Este paso implica copiar el código del repositorio ede Git que contiene el módulo de instalacion en el 
  directorio **'extra-addons'**. Para hacerlo, utiliza el comando:
  
      'git clone https://github.com/utrillas/odoo_instalacion.git'
      
  Esto descargará el código del repositorio y lo colocará en una carpeta llamada 'instalacion' dentro del      directorio 'extra_addons'.

Una vez hemos realizado los pasos anteriores, el módulo lo tendrás en el listado de aplicaciones de Odoo, realizas la busqueda del módulo 'instalacion', e instalas el módulo y ya lo tienes a tu disposición.

LLegado a este momento, se debe de dar los permisos según los roles de se desempeñe en la empresa:

  **- Director Regional**:
        El director regional tiene permisos en todos los modelos creados.

  **-Manager**:
        Los Project Manager tienen también todos los permisos creados.

  **-Coordinador**:
        Los coordinadores solamente tendrán permisos en los siguientes modelos:
- **instalacion**: Tienen permisos para crear, leer y escribir.
- **work_order**: Tienen permisos para crear, leer y escribir.
- **employee**: Tienen permisos para leer.
- **material**: Tienen permisos para leer y escribir.
- **reserve_line(material)**: Tienen permisos para leer, escribir y borrar.
- **work_order_employee**: Tienen permisos para leer, escribir y borrar.
- **reserve_material**: Tienen permisos para leer, escribir y borrar.
- **employee_line**: Tienen permisos para leer.


          
 **-Secretaria**:
       Las secretarias tienen los siguientes permisos:
  - **instalacion**: tienen permisos para crear/leer/escribir.
  - **work_order**: tienen permisos para crear/leer/escribir.
  - **employee**: tienen permisos para crear/leer/escribir.
  - **material**: tienen permisos para crear/leer/escribir.
  - **reserve_line(material)**: tienen permisos para crear/leer/escribir.
  - **work_order_employee**: tienen permisos para leer/escribir.
  - **reserve_material**: tienen permisos para leer/escribir/borrar.
  - **employee_line**: tienen permisos para crear/leer/escribir.
          
  **Documentacion**:
        El técnicos de documentación tiene los siguientes permisos:
  - **instalacion** tienen permisos para leer/escribir.
  - **work_order**: tienen permisos para crear/leer/escribir.
  - **employee**: tienen permisos para leer.
  - **material**: tienen permisos para leer/escribir.
  - **reserve_line(material)**: tienen permisos para crear/leer/escribir.
  - **work_order_employee**: tienen permisos para leer/escribir.
  - **reserve_material**: tienen permisos para crear/leer/escribir.
  - **employee_line**: tienen permisos para leer.

  **Tecnicos**:
          Los técnicos tiene los siguientes permisos:
  - **instalacion**: tienen permisos para leer.
  - **work_order**: tienen permisos para leer.
  - **employee**:  no tienen permisos.
  - **material**: no tienen permisos.
  - **reserve_line(material)**: tienen permisos paraleer.
  - **work_order_employee**: tienen permisos para leer.
  - **reserve_material**: tienen permisos paraleer.
  - **employee_line**: no tienen permisos.
            
  **Grupo Base**:
        Sólamente tienen permisos de lectura en todos los modelos.

            
