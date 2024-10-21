INSERT INTO domicilio (calle, altura, ciudad, pais)
VALUES 
('Principal', 111, 'Cordoba', 'Argentina'),
('Secundaria', 222, 'Buenos Aires', 'Argentina'),
('Terciaria', 333, 'Santiago', 'Chile'),
('Cuarta', 444, 'Montevideo', 'Uruguay'),
('Quinta', 555, 'Asuncion', 'Paraguay'),
('Sexta', 666, 'Cordoba', 'Argentina'),
('Septima', 777, 'Buenos Aires', 'Argentina'),
('Octava', 888, 'Santiago', 'Chile'),
('Novena', 999, 'Montevideo', 'Uruguay'),
('Decima', 101, 'Asuncion', 'Paraguay'),
('calle a', 111, 'Cordoba', 'Argentina'),
('calle b', 222, 'Buenos Aires', 'Argentina'),
('calle c', 333, 'Cordoba', 'Argentina'),
('calle d', 444, 'Buenos Aires', 'Argentina'),
('calle e', 555, 'Montevideo', 'Uruguay');

INSERT INTO punto_encuentro (nombre, ID_domicilio, descripcion)
VALUES 
('Punto Principal', 1, 'Centro comercial'),
('Punto Secundario', 2, 'Plaza pública'),
('Punto Terciario', 3, 'Café al lado del banco'),
('Punto Cuarto', 4, 'Centro vecinal'),
('Punto Quinto', 5, 'Polideportivo público'),
('Punto Sexto', 6, 'Centro juvenil de la ciudad'),
('Punto Séptimo', 7, 'Escalinatas Plaza España'),
('Punto Octavo', 8, 'Patio interno universidad');

INSERT INTO usuario (nombre_usuario, nombre, apellido, fecha_nacimiento, telefono, e_mail, password, ID_domicilio)
VALUES 
('amartinez', 'Alejandro', 'Martinez', '2001-01-01', '1111111111', 'mail1@mail1.com', 'passusuario1', 11),
('lgonzalez', 'Lucia', 'Gonzalez', '2002-01-02', '1122222222', 'mail2@mail2.com', 'passusuario2', 12),
('cherrera', 'Carlos', 'Herrera', '1990-02-01', '3511111111', 'mail3@mail3.com', 'passusuario3', 13),
('mfernandez', 'Maria', 'Fernandez', '1900-01-07', '3811111111', 'mail4@mail4.com', 'passusuario4', 14),
('jlopez', 'Javier', 'Lopez', '1987-09-25', '3512222222', 'mail5@mail5.com', 'passusuario5', 9);

INSERT INTO libro (titulo, autor, editorial, fecha_publicacion, genero, ID_usuario)
VALUES 
('Los desposeídos', 'Ursula K. LeGuin', 'Harper & Row', '1974-05-01', 'Ciencia ficción', 1),
('El hombre ilustrado', 'Ray Bradbury', 'Doubleday', '1951-02-01', 'Ciencia ficción', 1),
('El lobo estepario', 'Hermann Hesse', 'S. Fisher Verlag', '1927-09-01', 'Ficción filosófica', 2),
('La insoportable levedad del ser', 'Milan Kundera', 'Harper & Row', '1984-04-01', 'Ficción filosófica', 3),
('La broma', 'Milan Kundera', 'Gallimard', '1967-10-01', 'Sátira', 5),
('Boquitas pintadas', 'Manuel Puig', 'Editorial Jorge Alvarez', '1969-08-01', 'Ficción romántica', 4),
('La mano izquierda de la oscuridad', 'Ursula K. LeGuin', 'Ace Books', '1969-03-01', 'Ciencia ficción', 4),
('62 modelo para armar', 'Julio Cortázar', 'Sudamericana', '1968-07-01', 'Ficción experimental', 3),
('El amor en los tiempos del cólera', 'Gabriel García Márquez', 'Sudamericana', '1985-05-01', 'Novela romántica', 5),
('Informe sobre la Tierra: fundamentalmente inofensiva', 'Douglas Adams', 'Pan Books', '1992-10-01', 'Ciencia ficción', 2),
('Ana Karenina', 'León Tolstói', 'Revista Sovremennik', '1985-01-01', 'Novela realista', 1),
('Crimen y castigo', 'Fyodor Dostoevsky', 'The Russian Messenger', '1990-01-01', 'Ficción psicológica', 3);

INSERT INTO intercambio (fecha_intercambio, ID_usuario1, ID_libro1, ID_usuario2, ID_punto_encuentro)
VALUES 
('2024-06-01', 1, 1, 3, 4),
('2024-06-12', 2, 3, 4, 7),
('2024-01-26', 2, 10, 4, 6);