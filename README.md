# Proyecto Integrador - ISPC - Tecnicatura de Ciencia de Datos y Machine Learning.

## Segunda Evidencia.

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
### Proyecto Elegido: Sharing Books.
#### Descripción:
La aplicación que desarrollaremos en el presente proyecto permite a dos usuarios intercambiar libros, fomentando la creación de una comunidad de lectores promoviendo la interacción social y el intercambio cultural a través de la literatura.
El intercambio se hará en una ubicación específica, donde los usuarios se pongan de acuerdo para encontrarse. Se perimitirá intercambio de uno a uno, y se llevará registro de ese intercambio a través de ua hora y fecha. 
De los usuarios, tendremos registros sobre sus datos personales, incluyendo nombre y apellido, direccion, numero de contacto y un correo electrónico.
De los libros.

## Entrega Final

### Scafolding

1. **Carpeta Raíz**: Directorio donde se encuentran todos los archivos del programa.
	1. **Carpeta "Modules"**: Directorio donde se encuentran los CRUD de cada entidad.
		1. **Archivo __init__.py**: Archivo encargado de generar los imports para elementos fuera de modules.
		2. **Carpeta Address**: Directorio con archivos para entidad "domicilio".
			1. **CreateAddress.py**: Archivo donde se encuentra la función que se encarga de la creación de entidad domicilio.
			2. **UpdateAddress.py**: Archivo donde se encuentra la función que se encarga de la modificación de entidad domicilio.
		3. **Carpeta Books**: Directorio con archivos para entidad "libros".
			1. **CreateBook.py**: Archivo donde se encuentra la función que se encarga de la creación de entidad libro.
			2. **UpdateBook.py**: Archivo donde se encuentra la función que se encarga de la modificación de entidad libro.
			3. **GetBooks.py**: Archivo donde se encuentra la función que se encarga de la obtención de entidades libros.
			4. **DeleteBook.py**: Archivo donde se encuentra la función que se encarga del borrado de entidad libros.
		4. **Carpeta Swap**: Directorio con archivos para entidad "intercambio".
			1. **CreateSwap.py**: Archivo donde se encuentra la función que se encarga de la creación de entidad intercambio.
			2. **UpdateSwap.py**: Archivo donde se encuentra la función que se encarga de la modificación de entidad intercambio.
			3. **GetSwaps.py**: Archivo donde se encuentra la función que se encarga de la obtención de entidades intercambio.
			4. **DeleteSwap.py**: Archivo donde se encuentra la función que se encarga del borrado de entidad intercambio.
		5. **Carpeta Meeting**: Directorio con archivos para entidad "punto de encuentro".
			1. **CreateMeeting.py**: Archivo donde se encuentra la función que se encarga de la creación de entidad punto de encuentro.
			2. **UpdateMeeting.py**: Archivo donde se encuentra la función que se encarga de la modificación de entidad punto de encuentro.
			3. **GetMeeting.py**: Archivo donde se encuentra la función que se encarga de la obtención de entidades puntos de encuentro.
			4. **DeleteMeeting.py**: Archivo donde se encuentra la función que se encarga del borrado de entidad punto de encuentro.
		6. **Carpeta Users**: Directorio con archivos para entidad "usuarios".
			1. **CreateUser.py**: Archivo donde se encuentra la función que se encarga de la creación de entidad usuario.
			2. **UpdateUser.py**: Archivo donde se encuentra la función que se encarga de la modificación de entidad usuario.
			3. **GetUser.py**: Archivo donde se encuentra la función que se encarga de la obtención de entidades usuarios.
			4. **DeleteUser.py**: Archivo donde se encuentra la función que se encarga del borrado de entidad usuario.
		7. **Carpeta Utils**: Directorio con archivos para utilizaciones generales.
			1. **DateMask.py**: Archivo donde se encuentra la función que se encarga de crear y validar la fecha.
			2. **dBConnection.py**: Archivo donde se encuentra la función que se encarga crear el patrón Singleton para la conexión de BBDD.
	2. **Carpeta .venv:** Carpeta que carga los elementos necesarios para interpretar el lenguaje de python, conocido como *"Virtual Enviroment"*.
	3. **DB**: Carpeta donde se encuentran todos los elementos de la BBDD.
	4. **Archivo .env**: Archivo de variables de ambiente, necesario para conectar con la BBDD.
	5. **Archivo .gitignore**: Archivo encargado de apuntar los archivos que no deben ser pusheados al repositorio remoto de git.
	6. **main.py**: Archivo raíz del proyecto. En el se encuentra el menú principal y es por donde arranca la ejecución.
### Instalación de dependencias.

Luego de descargar el repositorio, debemos hacer una instalación de ciertas dependencias obligatorias para que pueda ejecutar el proyecto:
	 ` pip install prompt_toolkit `
	 ` pip install python-dotenv ` 
	 ` pip install mysql-connector-python `
Con estos comandos ya podremos ejecutarlo.

### Utilización de la Aplicación.

Para utilizar la aplicación, ejecutar desde main.py
Se desplegara en consola un menu numerico.
Elegir las opciones que uno quiera utilizar a medida que avanza por el proceso.
