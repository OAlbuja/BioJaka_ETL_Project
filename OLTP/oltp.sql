-- Creación de la base de datos
-- Se ajustar la tabla ProduccionInsumos para que no haga referencia a las tablas Hormonas y Reactivos, que ya no existen.

CREATE DATABASE IF NOT EXISTS oltp;
USE oltp;

-- Creación de la tabla Procesos
CREATE TABLE Procesos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    descripcion TEXT
);

-- Creación de la tabla Fases
CREATE TABLE Fases (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    duracion_estimada INT UNSIGNED COMMENT 'Duración estimada en días',
    proceso_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (proceso_id) REFERENCES Procesos(id),
    INDEX idx_proceso_id (proceso_id)
);

-- Creación de la tabla Lotes
CREATE TABLE Lotes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL UNIQUE,
    planta VARCHAR(100) NOT NULL,
    cantidad_medio DECIMAL(10, 2) NOT NULL,
    fase_id INT UNSIGNED NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    FOREIGN KEY (fase_id) REFERENCES Fases(id),
    INDEX idx_fase_id (fase_id),
    CHECK (cantidad_medio > 0)
);

-- Creación de la tabla Medios
CREATE TABLE Medios (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('Medio de cultivo', 'MS', 'Otro') NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    CHECK (costo >= 0)
);

-- Creación de la tabla ServiciosBasicos
CREATE TABLE ServiciosBasicos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('Agua', 'Electricidad', 'Internet', 'Otro') NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL,
    CHECK (costo >= 0)
);

-- Creación de la tabla Maquinas
CREATE TABLE Maquinas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    modelo VARCHAR(100) NOT NULL,
    eficiencia DECIMAL(5, 2) NOT NULL,
    fecha_adquisicion DATE NOT NULL,
    CHECK (eficiencia BETWEEN 0 AND 100)
);

-- Creación de la tabla ConsumoEnergia
CREATE TABLE ConsumoEnergia (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    maquina_id INT UNSIGNED NOT NULL,
    consumo_kwh DECIMAL(10, 2) NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (maquina_id) REFERENCES Maquinas(id),
    INDEX idx_maquina_id (maquina_id),
    CHECK (consumo_kwh >= 0),
    CHECK (costo >= 0)
);

-- Creación de la tabla Personal
CREATE TABLE Personal (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    cargo VARCHAR(100) NOT NULL,
    fecha_ingreso DATE NOT NULL
);

-- Creación de la tabla AsignacionPersonal
CREATE TABLE AsignacionPersonal (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    personal_id INT UNSIGNED NOT NULL,
    fecha DATE NOT NULL,
    horas_trabajo TINYINT UNSIGNED NOT NULL,
    remuneracion DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (personal_id) REFERENCES Personal(id),
    INDEX idx_personal_id (personal_id),
    CHECK (horas_trabajo > 0 AND horas_trabajo <= 24),
    CHECK (remuneracion >= 0)
);

-- Creación de la tabla Produccion
CREATE TABLE Produccion (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    plantas_producidas INT UNSIGNED NOT NULL,
    lote_id INT UNSIGNED NOT NULL,
    fase_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (lote_id) REFERENCES Lotes(id),
    FOREIGN KEY (fase_id) REFERENCES Fases(id),
    INDEX idx_lote_id (lote_id),
    INDEX idx_fase_id (fase_id),
    CHECK (plantas_producidas >= 0)
);

-- Creación de la tabla ProduccionInsumos
CREATE TABLE ProduccionInsumos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    produccion_id INT UNSIGNED NOT NULL,
    medio_id INT UNSIGNED,
    cantidad_usada DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (produccion_id) REFERENCES Produccion(id),
    FOREIGN KEY (medio_id) REFERENCES Medios(id),
    INDEX idx_produccion_id (produccion_id),
    CHECK (cantidad_usada > 0)
);

-- Creación de la tabla ProduccionServicios
CREATE TABLE ProduccionServicios (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    produccion_id INT UNSIGNED NOT NULL,
    servicio_id INT UNSIGNED NOT NULL,
    consumo_energia_id INT UNSIGNED,
    FOREIGN KEY (produccion_id) REFERENCES Produccion(id),
    FOREIGN KEY (servicio_id) REFERENCES ServiciosBasicos(id),
    FOREIGN KEY (consumo_energia_id) REFERENCES ConsumoEnergia(id),
    INDEX idx_produccion_id (produccion_id)
);

-- Creación de la tabla ProduccionPersonal
CREATE TABLE ProduccionPersonal (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    produccion_id INT UNSIGNED NOT NULL,
    asignacion_personal_id INT UNSIGNED NOT NULL,
    FOREIGN KEY (produccion_id) REFERENCES Produccion(id),
    FOREIGN KEY (asignacion_personal_id) REFERENCES AsignacionPersonal(id),
    INDEX idx_produccion_id (produccion_id),
    INDEX idx_asignacion_personal_id (asignacion_personal_id)
);


-- Todos los SELECT de las tablas para testear que funcione el script con FAKER
-- SELECT * FROM Procesos;
-- SELECT * FROM Fases;
-- SELECT * FROM Lotes;
-- SELECT * FROM Medios;
-- SELECT * FROM Hormonas;
-- SELECT * FROM Reactivos;
-- SELECT * FROM ServiciosBasicos;
-- SELECT * FROM Maquinas;
-- SELECT * FROM ConsumoEnergia;
-- SELECT * FROM Personal;
-- SELECT * FROM AsignacionPersonal;
-- SELECT * FROM Produccion;
-- SELECT * FROM ProduccionInsumos;
-- SELECT * FROM ProduccionServicios;
-- SELECT * FROM ProduccionPersonal;
