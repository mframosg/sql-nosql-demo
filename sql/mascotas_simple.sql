-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS mascotas;
USE mascotas;

-- 2. Tabla de dueños
CREATE TABLE duenos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- 3. Tabla de razas
CREATE TABLE razas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tamano ENUM('pequeño', 'mediano', 'grande') NOT NULL
);

-- 4. Tabla de mascotas (con relación a dueños y razas)
CREATE TABLE mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT,
    genero ENUM('Macho', 'Hembra'),
    dueno_id INT,
    raza_id INT,
    FOREIGN KEY (dueno_id) REFERENCES duenos(id) ON DELETE SET NULL,
    FOREIGN KEY (raza_id) REFERENCES razas(id)
);

-- 5. Insertar datos de ejemplo
-- Insertar dueños
INSERT INTO duenos (nombre, telefono, email) VALUES
('Miguel Ramos', '3101234567', 'miguel@email.com'),
('Juan García', '3209876543', 'juan@email.com');

-- Insertar razas
INSERT INTO razas (nombre, tamano) VALUES
('Golden Retriever', 'mediano'),
('Rottweiler', 'grande'),
('Pastor Alemán', 'grande'),
('Chihuahua', 'pequeño');

-- Insertar mascotas
INSERT INTO mascotas (nombre, edad, genero, dueno_id, raza_id) VALUES
('Max', 3, 'Macho', 1, 1),    
('Luna', 2, 'Hembra', 1, 2),
('Toby', 4, 'Macho', 2, 3),  
('Bella', 1, 'Hembra', Null, 4);

-- 6. Consultas útiles
-- Mostrar todas las mascotas con sus dueños y razas
SELECT 
    m.nombre AS mascota,
    m.edad,
    m.genero,
    d.nombre AS dueno,
    r.nombre AS raza,
    r.tamano
FROM 
    mascotas m
LEFT JOIN 
    duenos d ON m.dueno_id = d.id
LEFT JOIN 
    razas r ON m.raza_id = r.id;

-- Mostrar mascotas sin dueño (Bella aparece aquí porque se insertó sin dueño)
SELECT * FROM mascotas WHERE dueno_id IS NULL;

UPDATE mascotas
SET dueno_id = 1
WHERE nombre = 'Bella';

-- Contar mascotas por dueño
SELECT 
    d.nombre AS dueno,
    COUNT(m.id) AS total_mascotas
FROM 
    duenos d
LEFT JOIN 
    mascotas m ON d.id = m.dueno_id
GROUP BY 
    d.id, d.nombre;

-- 7. Eliminar todo (descomentar solo si es necesario)
-- DROP TABLE IF EXISTS mascotas;
-- DROP TABLE IF EXISTS duenos;
-- DROP TABLE IF EXISTS razas;
-- DROP DATABASE IF EXISTS mascotas;

