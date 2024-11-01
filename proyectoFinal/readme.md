# Proyecto Final - ISPC - Módulo Innovación en Gestión de Datos

### Integrantes
1. Integrante 1:
	- **Nombre:** Kuttel, Matías Agustín.
	- **DNI:** 39301933.
	- **Email:** lejesterdelacorte@gmail.com
	- **GitHub**: https://github.com/lejesterdelacorte
2. Integrante 2:
	- **Nombre:** Molina, Jonathan Ariel.
	- **DNI:** 32623883.
	- **Email:** jonathanarmol@gmail.com
	- **GitHub**: https://github.com/Jonaarmol
3. Integrante 3:
	- **Nombre:** Albors, Ezequiel.
	- **DNI:** 38501932
	- **Email:** ezequielalbors@gmail.com
	- **GitHub**:  https://github.com/eze3221
5. Integrante 4:
	- **Nombre:** Asef, Nicolás.
	- **DNI:** 39070521
	- **Email:** nicolasasef1@gmail.com
	- **GitHub**: https://github.com/nicolas-asef


## Sistema de Gestión de Usuarios y Accesos en Python

## Descripción

Se presenta el trabajo final del módulo "Innovación en Gestión de datos". Se trata de una aplicación de consola en Python que implementa un sistema de gestión de usuarios y accesos. Utiliza Programación Orientada a Objetos (POO), archivos binarios para el almacenamiento de datos y CRUD sobre usuarios. Además se pueden registrar accesos exitosos y fallidos y gestionar los intentos de acceso al sistema.  
Por otra parte se trabajó con la conexión a la base de datos del proyecto "Sharing Books" para cumplir las consignas planteadas para Bases de Datos. Se la incluyó en el menú principal a través de un sub-menú, el cual permite acceder a las consultas SQL que se implementaron en la evidencia n°2/3.
Por último se incluyó un submenú de análisis de datos en donde se cumplen las consignas de uso de la librería Matplotlib, Pandas y Nunpy.  


## Archivos Binarios:

usuarios.ispc: Almacena los datos de los usuarios.
accesos.ispc: Almacena los registros de accesos exitosos.
logs.txt: Almacena los intentos fallidos de ingreso.
usuariosOrdenadosPorUsername.ispc: Guarda los usuarios ordenados alfabéticamente por su username cuando se elige específicamente la opción.
buscandoUsuarioPorUsername-fecha.txt: Registro de cada intento de búsqueda binaria por username, detallando comparaciones realizadas y decisiones tomadas.
buscandoUsuarioPorDNI-fecha.txt: Archivo de seguimiento de la búsqueda binaria por DNI, que documenta comparaciones, decisiones de búsqueda (izquierda o derecha), y si el usuario fue encontrado o no.

## Base de Datos:

Se implementa un submenú adicional que realiza consultas a la base de datos del proyecto "Sharing Books". Se pueden ejecutar operaciones SELECT, INSERT, UPDATE, DELETE y JOIN relacionadas con libros y usuarios.

## Funcionalidades

Gestión de Usuarios (CRUD): Crear nuevos usuarios. Modificar usuarios existentes. Eliminar usuarios (por username o email). Buscar usuarios (por username o email o DNI). Mostrar todos los usuarios registrados.
Gestión de Accesos: Registro de accesos exitosos. Registro de intentos fallidos en logs.txt.
Acceso al Sistema: Solicitud de username y password para ingresar. Registro de cada acceso exitoso en accesos.ispc. Registro de intentos fallidos en logs.txt, incluyendo la fecha y los datos ingresados.
Conexión a la Base de Datos: Consulta de usuarios y libros en la base de datos de Sharing Books. Operaciones CRUD sobre los libros y los usuarios almacenados en la base de datos.

## Requisitos

Para que la aplicación funcione correctamente, es necesario instalar los siguientes componentes:

Python 3.x
Módulos requeridos:
random: para generación de registros pluviales.
pickle: Para la manipulación de archivos binarios.
os: Para operaciones relacionadas con el sistema de archivos.
datetime: Para la gestión de fechas en el registro de accesos.
mysql-connector-python: Para la conexión a la base de datos MySQL.
librerías: Pandas/Matplotlib/Nunpy.

## Configuración de la Base de Datos

Archivo .env: El proyecto utiliza un archivo .env para almacenar las credenciales de acceso a la base de datos.
Base de Datos MySQL: Se trabaja con la base de datos del proyecto "Sharing Books" y para ello, favor de ejecutar los scripts de creación de tablas (ScriptCreacionDB.sql) y de inserción de datos iniciales (InsercionDatos.sql).


## Uso

Menú Principal

Al ejecutar el main.py, se mostrará el siguiente menú:

Usuarios y Accesos de la Aplicación: Permite acceder al CRUD de usuarios; mostrar datos de accesos; ordenamiento y búsqueda de usuarios.
Ingresar al sistema con los datos de usuario: Solicita el username y password para ingresar al sistema y registrar el acceso; también se accede a la gestión de la base de datos del proyecto "Sharing books" en donde permite realizar consultas SQL sobre libros y usuarios de la base de datos.
Análisis de datos: Permite ejecutar el análisis de datos según el año/mes de interés del usuario.
Salir de la aplicación: Permite salir de la aplicación. 