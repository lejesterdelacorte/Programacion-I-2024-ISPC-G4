Sistema de Gestión de Usuarios y Accesos en Python

Descripción

Se presenta la evidencia de aprendizaje n°3. Se trata de una aplicación de consola en Python que implementa un sistema de gestión de usuarios y accesos. Utiliza Programación Orientada a Objetos (POO), archivos binarios para el almacenamiento de datos y CRUD sobre usuarios. Además se pueden registrar accesos exitosos y fallidos y gestionar los intentos de acceso al sistema.  
Por otra parte se trabajó con la conexión a la base de datos del proyecto "Sharing Books" para cumplir las consignas planteadas para Bases de Datos. Se la incluyó en el menú principal a través de un sub-menú, el cual permite acceder a las consultas SQL que se implementaron en la evidencia n°2.
Por último se incluyeron 3 archivos relacionados a las consignas de Programación sobre registros pluviales y uso de la librería Matplotlib que no fueron integrados al menú principal.  


Archivos Binarios:

usuarios.ispc: Almacena los datos de los usuarios.
accesos.ispc: Almacena los registros de accesos exitosos.
logs.txt: Almacena los intentos fallidos de ingreso.

Base de Datos:

Se implementa un submenú adicional que realiza consultas a la base de datos del proyecto "Sharing Books". Se pueden ejecutar operaciones SELECT, INSERT, UPDATE, DELETE y JOIN relacionadas con libros y usuarios.

Funcionalidades

Gestión de Usuarios (CRUD): Crear nuevos usuarios. Modificar usuarios existentes. Eliminar usuarios (por username o email). Buscar usuarios (por username o email). Mostrar todos los usuarios registrados.
Gestión de Accesos: Registro de accesos exitosos. Registro de intentos fallidos en logs.txt.
Acceso al Sistema: Solicitud de username y password para ingresar. Registro de cada acceso exitoso en accesos.ispc. Registro de intentos fallidos en logs.txt, incluyendo la fecha y los datos ingresados.
Conexión a la Base de Datos: Consulta de usuarios y libros en la base de datos de Sharing Books. Operaciones CRUD sobre los libros y los usuarios almacenados en la base de datos.

Requisitos

Para que la aplicación funcione correctamente, es necesario instalar los siguientes componentes:

Python 3.x
Módulos requeridos:
random: para generación de registros pluviales.
pickle: Para la manipulación de archivos binarios.
os: Para operaciones relacionadas con el sistema de archivos.
datetime: Para la gestión de fechas en el registro de accesos.
mysql-connector-python: Para la conexión a la base de datos MySQL.
librerías: Pandas/Matplotlib.

Configuración de la Base de Datos

Archivo .env: El proyecto utiliza un archivo .env para almacenar las credenciales de acceso a la base de datos.
Base de Datos MySQL: Se trabaja con la base de datos del proyecto "Sharing Books" y para ello, favor de ejecutar los scripts de creación de tablas (Ev3_ScriptCreacionDB.sql) y de inserción de datos iniciales (EV3_InsercionDatos.sql).
Implementación de sugerencias Evidencia n°2: 
-Se crearon las vistas e index sugeridos. 
-Se modificó el tipo de dato de "altura" de la tabla "domicilio".
-Se cambió el nombre a "hashed_password" en la tabla "usuario".
-Se agregaron "ipAddress", "deviceInfo" en "acceso" para inclui más detalles.


Uso

Menú Principal

Al ejecutar el main.py, se mostrará el siguiente menú:

Crear nuevo usuario: Permite agregar un usuario con username, password y email.
Modificar usuario: Modifica la información de un usuario existente.
Eliminar usuario: Elimina un usuario dado su username o email.
Buscar usuario: Busca un usuario por su username o email.
Mostrar todos los usuarios: Muestra todos los usuarios registrados.
Ingresar al sistema: Solicita el username y password para ingresar al sistema y registrar el acceso.
Ordenamiento de usuarios: Permite ordenar los usuarios por "Username" brindando las opciones de realizarlo a través del algoritmo "Bubble" y por el método sort() de Python.  
Conexión con base de datos de Sharing Books: Submenú que permite realizar consultas SQL sobre libros y usuarios de la base de datos.
Salir: Finaliza la aplicación.

Submenú de Conexión con la Base de Datos

Este submenú permite realizar las siguientes operaciones en la base de datos del proyecto Sharing Books:

Mostrar libros por género: Muestra la lista de libros almacenados en la base de datos según el género ingresado mediante un input.
Insertar nuevo usuario: Permite agregar un nuevo usuario.
Modificar teléfono de un usuario: Permite modificar el número telefónico de un usuario particular.
Eliminar libro: Permite eliminar un libro dado su ID.
Buscar libros por usuario: Realiza un JOIN entre usuarios y libros para mostrar los libros registrados por un usuario específico.
Buscar domicilios de puntos de encuentro: Realiza un JOIN entre domicilio y puntos de encuentro para mostrar los puntos de encuentro y sus direcciones. 

Archivos de registros pluviales

No se incluyó la resolución de las consignas en el menú principal de la aplicación ya que por la información publicada en el foro de la evidencia n°3, se interpretó que era una actividad propuesta para practicar el uso de la librería Matplotlib y la generación de archivos .csv. Se detallan los archivos: 

registrosAleatorios.py : creación aleatoria de datos para el archivo .csv mediante el módulo "Random" y la librería Pandas.
cargarRegistros.py : carga los datos aleatorios y genera el archivo .csv.
consignasMatplotlib.py : en este archivo se llevan a cabo las consignas propuestas sobre la librería Matplotlib valiéndose de los datos del archivo registrosPluviales2023.csv generado previamente.
registrosPluviales2023.csv : archivo .csv generado tras la ejecución de los anteriores archivos .py.

Notas

-Los archivos binarios usuarios.ispc y accesos.ispc se crearán automáticamente al ejecutar el programa por primera vez.
-El archivo logs.txt almacenará los intentos fallidos de acceso, incluyendo la fecha y los datos ingresados.
-En las pruebas se detecta un bug donde al optar por 2) Modificar usuario, la excepción correspondiente a un id no existente (o eliminado) no es arrojada hasta que todos los datos son solicitados. Se considera de relevancia menor, ya que el programa no permite de todos modos alterar el registro que no debería alterarse. Se modificará para la presentación del proyecto final. 