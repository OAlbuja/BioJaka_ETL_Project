-- Base de Datos Dimensional
CREATE DATABASE IF NOT EXISTS sor;
USE sor;

-- Tabla de Dimensión de Tiempo
CREATE TABLE Dim_Tiempo (
    tiempo_id INT PRIMARY KEY,
    fecha DATE,
    año INT,
    trimestre INT,
    mes INT,
    día INT,
    día_semana VARCHAR(10)
);

-- Tablas de Dimensiones
CREATE TABLE Dim_Maquinas (
    maquina_id INT PRIMARY KEY,
    nombre VARCHAR(255),
    modelo VARCHAR(255),
    eficiencia DECIMAL(5,2),
    fecha_adquisicion DATE
);

CREATE TABLE Dim_Personal (
    personal_id INT PRIMARY KEY,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    cargo VARCHAR(255),
    fecha_ingreso DATE
);

CREATE TABLE Dim_Fases (
    fase_id INT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion TEXT,
    duracion_estimada INT
);

CREATE TABLE Dim_Procesos (
    proceso_id INT PRIMARY KEY,
    nombre VARCHAR(255),
    descripcion TEXT
);

-- Tabla de Dimensión de Insumos
CREATE TABLE Dim_Insumos (
    insumo_id INT PRIMARY KEY,
    nombre VARCHAR(255),
    tipo ENUM('Medio', 'Hormona', 'Reactivo'),
    categoria ENUM('Enraizamiento', 'Multiplicación', 'Agua Jabonosa', 'Alcohol', 'Otro'),
    costo DECIMAL(10,2)
);

-- Tabla de Hechos de Producción y Consumo
CREATE TABLE Fact_ProduccionConsumo (
    produccion_id INT PRIMARY KEY,
    tiempo_id INT,
    maquina_id INT,
    personal_id INT,
    fase_id INT,
    proceso_id INT,
    insumo_id INT,  -- Asegúrate de que este campo sea INT
    lote_codigo VARCHAR(50),
    planta VARCHAR(100),
    plantas_producidas INT,
    consumo_kwh DECIMAL(10, 2),
    costo_total_insumos DECIMAL(10, 2),
    costo_servicios DECIMAL(10, 2),
    costo_personal DECIMAL(10, 2),
    FOREIGN KEY (tiempo_id) REFERENCES Dim_Tiempo(tiempo_id),
    FOREIGN KEY (maquina_id) REFERENCES Dim_Maquinas(maquina_id),
    FOREIGN KEY (personal_id) REFERENCES Dim_Personal(personal_id),
    FOREIGN KEY (fase_id) REFERENCES Dim_Fases(fase_id),
    FOREIGN KEY (proceso_id) REFERENCES Dim_Procesos(proceso_id),
    FOREIGN KEY (insumo_id) REFERENCES Dim_Insumos(insumo_id) -- Asegúrate de que este campo sea INT
);
