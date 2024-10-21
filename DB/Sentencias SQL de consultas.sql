/*Tabla, mostrando todos los datos:*/

SELECT * FROM domicilio;
SELECT * FROM usuario;
SELECT * FROM libro;
SELECT * FROM punto_encuentro;
SELECT * FROM intercambio;


/*Una sola tabla (mostrando algunas columnas):*/

SELECT id_libro, titulo, autor FROM libro;

/*Una sola tabla con where:*/

SELECT id_libro, titulo, autor FROM libro WHERE genero = "ciencia ficcion";

/*Una sola tabla con where utilizando between:*/

SELECT * FROM domicilio WHERE ID_domicilio BETWEEN 1 AND 5;

/*Una sola tabla con where utilizando limit:*/

SELECT * FROM punto_encuentro ORDER BY ID_punto_encuentro LIMIT 3;

/*Más de 1 tabla con inner join:*/

SELECT u.ID_usuario, u.nombre_usuario, l.ID_libro, l.titulo, l.autor, l.genero
FROM usuario u
INNER JOIN libro l ON u.ID_usuario;

SELECT u.ID_usuario, u.nombre_usuario, l.ID_libro, l.titulo, l.autor, l.genero
FROM usuario u
INNER JOIN libro ON u.ID_usuario = l.ID_usuario;

/*Más de 1 tabla con inner join y con filtros:*/

SELECT u.ID_usuario, u.nombre_usuario, l.ID_libro, l.autor, l.editorial, l.fecha_publicación, l.genero
FROM usuario u
INNER JOIN libro l ON u.ID_usuario = l.ID_usuario
WHERE l.editorial = 'sudamericana';

SELECT d.*, p.nombre AS nombre_punto_encuentro, p.descripcion
FROM domicilio d
INNER JOIN punto_encuentro p ON d.ID_domicilio = p.ID_domicilio
WHERE p.descripcion LIKE '%centro%';
