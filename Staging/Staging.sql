CREATE DATABASE IF NOT EXISTS staging;
USE staging;
 
CREATE TABLE ext_asignacionPersonal AS SELECT * FROM oltp.AsignacionPersonal WHERE 1=2;
CREATE TABLE ext_consumoEnergia AS SELECT * FROM oltp.ConsumoEnergia WHERE 1=2;
CREATE TABLE ext_fases AS SELECT * FROM oltp.Fases WHERE 1=2;
CREATE TABLE ext_lotes AS SELECT * FROM oltp.Lotes WHERE 1=2;
CREATE TABLE ext_maquinas AS SELECT * FROM oltp.Maquinas WHERE 1=2;
CREATE TABLE ext_medios AS SELECT * FROM oltp.Medios WHERE 1=2;
CREATE TABLE ext_personal AS SELECT * FROM oltp.Personal WHERE 1=2;
CREATE TABLE ext_procesos AS SELECT * FROM oltp.Procesos WHERE 1=2;
CREATE TABLE ext_produccion AS SELECT * FROM oltp.Produccion WHERE 1=2;
CREATE TABLE ext_produccion_insumos AS SELECT * FROM oltp.ProduccionInsumos WHERE 1=2;
CREATE TABLE ext_produccion_personal AS SELECT * FROM oltp.ProduccionPersonal WHERE 1=2;
CREATE TABLE ext_produccion_servicios AS SELECT * FROM oltp.ProduccionServicios WHERE 1=2;
CREATE TABLE ext_servicios_basicos AS SELECT * FROM oltp.ServiciosBasicos WHERE 1=2;

-- Crear las tablas Hormonas y Reactivos directamente en staging (Datos extraidos desde CSVs)
CREATE TABLE ext_hormonas (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('Enraizamiento', 'Multiplicación', 'Otro') NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    CHECK (costo >= 0)
);

CREATE TABLE ext_reactivos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo ENUM('Agua Jabonosa', 'Alcohol', 'Otro') NOT NULL,
    costo DECIMAL(10, 2) NOT NULL,
    CHECK (costo >= 0)
);
