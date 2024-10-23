Sistema de Gestión de Usuarios y Accesos en Python 

Descripción

Este proyecto es una aplicación de consola en Python que implementa un sistema de gestión de usuarios y accesos. Utiliza Programación Orientada a Objetos (POO) y archivos binarios para el almacenamiento de datos. Se pueden realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios, registrar accesos exitosos y fallidos, y gestionar los intentos de acceso al sistema.

Los datos se almacenan en archivos binarios:

usuarios.ispc: Almacena los datos de los usuarios.
accesos.ispc: Almacena los registros de accesos exitosos.
logs.txt: Almacena los intentos fallidos de ingreso.
Funcionalidades
Gestión de Usuarios (CRUD):

Crear nuevos usuarios.
Modificar usuarios existentes.
Eliminar usuarios (por username o email).
Buscar usuarios (por username o email).
Mostrar todos los usuarios registrados.
Gestión de Accesos:

Registro de accesos exitosos.
Registro de intentos fallidos en logs.txt.
Acceso al Sistema:

Solicitud de username y password para ingresar.
Registro de cada acceso exitoso en accesos.ispc.
Registro de intentos fallidos en logs.txt, incluyendo la fecha y los datos ingresados.

Requisitos

Python 3.x
Módulos estándar:
pickle
os
datetime

Uso

Menú Principal

Al ejecutar la aplicación, se mostrará el siguiente menú:

Crear nuevo usuario: Permite agregar un usuario con username, password y email.
Modificar usuario: Modifica la información de un usuario existente.
Eliminar usuario: Elimina un usuario dado su username o email.
Buscar usuario: Busca un usuario por su username o email.
Mostrar todos los usuarios: Muestra todos los usuarios registrados.
Ingresar al sistema: Solicita el username y password para ingresar al sistema y registrar el acceso.
Salir: Finaliza la aplicación.


Notas

Los archivos binarios usuarios.ispc y accesos.ispc se crearán automáticamente al ejecutar el programa por primera vez.
El archivo logs.txt almacenará los intentos fallidos de acceso, incluyendo la fecha y los datos ingresados.

En las pruebas se detecta un bug donde al optar por 2) Modificar usuario, la excepción correspondiente a un id no existente (o eliminado) en la db no es arrojada hasta que todos los datos son solicitados. 
Se considera de relevancia menor, ya que el programa no permite de todos modos alterar el registro que no debería alterarse.
Para futura iteración, se sugiere como posible solución modificar el método de "findUser" en "CrudUsuarios" para que acepte un id como parámetro de búsqueda en db. 