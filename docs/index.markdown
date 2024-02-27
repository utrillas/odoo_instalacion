---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
﻿# **Fase 04 – TELECOMUNICACIONES**

## 1. **Nombre del módulo:** 

    INSTALACIONES
        
        
## 2. **Descripción corta:** 

Módulo que esta pensado para la gestión integral de instalaciones de telefonia móvil, desde la llegada del pedido/trabajo, hasta la documentación final
sin olvidarnos de los procesos de elección de personal, gestión de material extra, material especial para el trabajo, información de todos los procesos
gestión de incidencias de material especial, comunicación de llegada del material de empresa madre y de la documentación tanto de los replanteos hasta
los trabajos finales, teniendo disponibilidad de los demás trabajos realizados en el mismo site para la misma empresa madre.


## 3. **Descripción detallada de todas las funcionalidades a cubrir:** 
- Introducción de datos del site con toda su equipación.
- Realizará informes, es decir, la información que se ha introducido podrá ser impresa y/o reenviada por correo.
- Se podrá planificar el trabajo de los trabajadores (técnicos de instalaciones / documentación) asignándoles PI.
- Tendrá una zona para poder generar un pedido a almacén con el material extra.
- Se abrirán las nuevas secciones si el visto bueno de la empresa madre existe.


## 4. **Mapa del módulo:**

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.001.png)

## 5. **Dependencias de otros módulos:**

Este modulo dependerá del módulo de empleados (Técnicos de instalaciones) y del módulo de almacén.

## 6. **Wireframe de las páginas a mostrar:**

Página inicial del modulo:

En esta página se iniciará el proceso con la selección de parámetros iniciales, como dar el ok al replanteo para que pueda ser editable la página de replanteo, o editable la página de obra. El gestor podrá realizar la planificación del replanteo y la obra, el envío de petición de material extra a almacén o la petición de compra al departamento de compras. En general, podrá realizarse todas las tareas necesarias para la planificación y realización de actividades desde el punto 0 de la obra hasta el acabo de la obra y entrega del informa a la empresa madre. Como se puede ver en el wireframe, seguiremos la estética que nos proporciona Odoo, la página del site podrá ya existir porque sea un site que ya esta, lo cual lo dejaremos reflajado en las preguntas iniciales o será completamente nuevo. En la primera pestaña será de gestión, para el Project Manager y el Gestor de la obra. Ademas de las acciones, que son las comunes de guardado, eliminación, etc, tendremos 3 botones donde tendremos el impreso de informe, la edición, y el envío vía email de resumen de los datos obtenidos. Aquí tendremos un step bar que nos informará de la llegada del material o de la preparación del material extra. Se pondrá en color verde una vez haya llegado.

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.002.png)

Página replanteo:

La segunda pestaña que encontramos es la de replanteo, donde el técnico de documentación tendrá que cumplimentarlo después de que el técnico de replante les haya llevado toda la información del replanteo del site, esta pestaña no será editable hasta que el Gestor no ponga una fecha de replanteo. En ella podemos ver primero una pregunta de si hay material reutilizable, y siendo así hay habrá una caja para poder poner toda la información, abajo veremos que hay una caja con parámetros generales que habrá obtenido el técnico de replanteo (será igual al checklist que se lleva el técnico para poder realizar el replanteo), además este tendrá que realizar reportaje fotográfico para introducirlo, cada fotografía en su sitio correspondiente, es decir, si se pide situación de las antenas, el técnico de replanteo hará una foto del sitio y se la enviará al técnico de documentación para que pueda introducirla. 

Una vez este completamente rellenada la página con los datos, se enviará un comunicado al Gestor de proyectos para que verifique el trabajo realizado y pueda pedir la verificación a la empresa madre. 

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.003.png)

Página petición a compras/almacén:

En esta nueva pestaña podremos pedir el material a almacén o en caso de que falte material, que aparecerá en rojo tanto si no hay material como que la cantidad que se necesite no sea suficiente con el stock actual, se le envíe directamente un mensaje al departamento de compras para que se ejecute el pedido. Además, hay un apartado para pedidos de material especial, cuando pulsamos encima de la línea, aparecerá una lista de posibles items y pulsaremos el que queramos modificar, tendremos planos disponibles para posibles modificaciones, los más habituales, y si no es parecido a ninguno de ellos tendremos un botón donde podemos introducir un plano con toda la información para que el departamento de compras lo evalúe con el Project Manager, o si es una cifra muy superior a los 1000 euros estipulados en compras, con el Director regional.

Además, en esas compras especiales tendremos una Step Bar, que nos informará en que proceso esta el material, si compras ha realizado el pedido, si la empresa ha fabricado el material, si lo ha enviado y si ya lo hemos recepcionado en almacén. En caso de que haya algún problema en cualquiera de los procesos, se pondrá en color amarillo y al pulsar aparecerá un mensaje que nos dirá cual es el problema.

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.004.png)Página RPL:Esta página será cumplimentada por el técnico de documentación con las indicaciones que le realice el gestor. Se introducirán los pdf que la empresa madre necesita para la gestión de PRL y se los técnicos necesarios para la obra, además de los RP y los reservas.

Esta página será la que le creará la información necesaria al Gestor para tener el listado de técnicos.

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.005.png)

Página Obra:

Una vez el gestor tenga la petición a almacén y sepa que tiene todo el material, podrá realizar la programación de la obra, que la realizará en la primera hoja, seleccionando los trabajadores disponibles gracias a los técnicos que se han introducido en la hoja de técnicos-prl. 

Una vez se ha finalizado la obra, los técnico hacen un informe de las variaciones que hayan con el replanteo para que el técnico de documentación pueda introducirlo en la hoja de la obra. Además los técnicos deberán de entregar las fotografías para que el técnico de 

documentación pueda generar la documentación de fin de obra.

Una vez el técnico de documentación ha terminado de documentar la obra, la envía al gestor para que pueda generar el informe para la empresa madre.

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.006.png)

## 7. **Controles de accesos. ¿Qué grupos existen? ¿Quién puede acceder o no al módulo? ¿A qué modelos? ¿a qué registros? ¿Con qué permisos?**

   Este modulo tendrá dos vistas, de visualización y de edición.

- Visualización: Los técnicos asignados a la obra podrán ver la hoja de replanteo para saber cual es el trabajo a realizar. Podrán bajarse tambien un pdf con toda la información.
- Edición: El project manager, el Gestor, y los técnicos de documentación podrán tener edición en este módulo.

  ◦ Los módulos serán visibles y editables solamente cuando en la página inicial se de el visto bueno a cada una de las partes. Solamente el Project Manager y el Gestor podrán editar la primera página, la página de petición de materialo extra también podrán editarla ellos, y la de replanteo y obra la editarán los 3 grupos (project manager, gestor y técnicos de documentación).

## 8. **Diagramas de flujo funcionales de las diferentes partes del módulo** 

### DIAGRAMA DEL MODULO COMPLETO.
======================================

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.007.png)

### PANTALLA MATERIAL EXTRA(1):
======================================

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.008.png)

### PANTALLA TECNICO-RP(2):
======================================

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.009.png)

### BOTON IMPRESORA:
======================================

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.010.png)

### BOTON EDICION:
======================================

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.011.png)

### BOTON CORREO:
======================================

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.012.png)

## 9. **Esquema relacional de las nuevas tablas en la base de datos y relación con otras existentes:**

![](Aspose.Words.ddb7d442-46ff-4c41-94c6-b90c6c6f2576.013.png)

## 10. **En el caso de que el módulo tenga como función la comunicación con otros módulos, indica las características de la comunicación: formato, estructura del mensaje, protocolo...:**

    módulo empleados: 

        La comunicación será un envío de un diccionario de los trabajadores  que sea   técnico y si tienen el curso de Recurso preventivo o no. 

    módulo almacén:

        La comunicación será un envío de un diccionario con los items y las unidades de estos. 
        
    módulo correo:

        Cuando se pulse el botón de correo, se abrirá el módulo de correo con una documento de pdf adjunto de la vista de ese momento (vista del replanteo, 
        vista del trabajo o vista  de la información inicial.)