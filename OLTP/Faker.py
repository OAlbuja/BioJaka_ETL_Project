from faker import Faker
import mysql.connector
from mysql.connector import Error
from datetime import timedelta, datetime

descripciones_procesos = [
    "Este proceso está diseñado para mejorar la eficiencia de la producción mediante la automatización.",
    "El objetivo de este proceso es reducir el tiempo de producción manteniendo los estándares de calidad.",
    "Este proceso involucra la implementación de nuevas tecnologías para incrementar la salida.",
    "Proceso dedicado a la optimización de recursos y materiales usados en la producción.",
    "Este proceso se centra en el cumplimiento de normativas ambientales y de seguridad."
]

descripciones_fases = {
    "Esta fase se centra en la planificación y establecimiento de los objetivos del proyecto.",
    "Durante esta fase, se desarrollan las soluciones y se realiza el trabajo principal.",
    "Esta fase implica la puesta en marcha del sistema y la integración con otros sistemas.",
    "Se realiza un control de calidad y se asegura que todo funcione según lo planeado.",
    "Finalización del proyecto, documentación y cierre de todas las actividades."
}

nombres_fases = [
    'Fase de Inicio',
    'Fase de Desarrollo',
    'Fase de Implementación',
    'Fase de Revisión',
    'Fase de Cierre'
]

# Crear la conexión con la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='10.10.10.2',  # Cambiado a la IP del servidor
            user='dwh',  # Cambiado al usuario correspondiente
            password='elcaro_4Q',  # Cambiado a la contraseña correspondiente
            database='oltp'  # Cambiado a 'oltp'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Función genérica para insertar datos en cualquier tabla
def insert_data(connection, query, data):
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

faker = Faker('es_MX')
conn = create_connection()

if conn is not None:
    for _ in range(100):
        # Tabla Procesos 1 x
        proceso_id = insert_data(conn, """
            INSERT INTO Procesos (nombre, fecha_inicio, fecha_fin, descripcion)
            VALUES (%s, %s, %s, %s);
            """, (
            faker.random_element(elements=('Proceso de Síntesis', 'Proceso de Extracción', 'Proceso de Fermentación', 'Proceso de Purificación', 'Proceso de Envasado')),
            faker.date_between(start_date="-1y", end_date="today"),
            faker.date_between(start_date="today", end_date="+1y"),
            faker.random_element(elements=(descripciones_procesos))
        ))

        # Tabla Fases 2
        fase_id = insert_data(conn, """
            INSERT INTO Fases (nombre, descripcion, duracion_estimada, proceso_id)
            VALUES (%s, %s, %s, %s);
            """, (
            faker.random_element(elements=(nombres_fases)),
            faker.random_element(elements=(descripciones_fases)),
            faker.random_int(min=1, max=180),
            proceso_id
        ))

        # Tabla Lotes 3
        lote_id = insert_data(conn, """
            INSERT INTO Lotes (codigo, planta, cantidad_medio, fase_id, fecha_inicio, fecha_fin)
            VALUES (%s, %s, %s, %s, %s, %s);
            """, (
            faker.bothify(text='???-###'),
            faker.random_element(elements=( 'Agave azul',
                                            'Rosa damascena',
                                            'Lavanda',
                                            'Eucalipto',
                                            'Aloe vera')),
            faker.pydecimal(left_digits=5, right_digits=2, positive=True),
            fase_id,
            faker.date_between(start_date="-1y", end_date="today"),
            faker.date_between(start_date="today", end_date="+1y")
        ))

        # Tabla Medios 4
        medio_id = insert_data(conn, """
            INSERT INTO Medios (nombre, tipo, costo)
            VALUES (%s, %s, %s);
            """, (
            faker.random_element(elements=('Nutriente X10',
                                            'Agar Especial',
                                            'Solución de Crecimiento',
                                            'Compuesto Hidropónico',
                                            'Bioestimulante Natural')),
            faker.random_element(elements=('Medio de cultivo', 'MS', 'Otro')),
            faker.pydecimal(left_digits=5, right_digits=2, positive=True)  # Corregido para usar pydecimal
        ))

        # Insertar en ServiciosBasicos 7 
        servicio_id = insert_data(conn, """
            INSERT INTO ServiciosBasicos (tipo, costo, fecha)
            VALUES (%s, %s, %s);
            """, (
            faker.random_element(elements=('Agua', 'Electricidad', 'Internet', 'Otro')),
            faker.pydecimal(left_digits=5, right_digits=2, positive=True),  # Corregido para usar pydecimal
            faker.date_between(start_date="-1y", end_date="today")
        ))

        # Insertar en Maquinas 8
        maquina_id = insert_data(conn, """
            INSERT INTO Maquinas (nombre, modelo, eficiencia, fecha_adquisicion)
            VALUES (%s, %s, %s, %s);
            """, (
            faker.random_element(elements=('Compresor Industrial',
                                            'Torno CNC',
                                            'Prensa Hidráulica',
                                            'Cortadora Láser',
                                            'Robot de Ensamblaje')),
            faker.bothify(text='Modelo ###??'),
            faker.random_number(digits=2),
            faker.date_between(start_date="-10y", end_date="today")
        ))

        # Insertar en Personal 9 
        personal_id = insert_data(conn, """
            INSERT INTO Personal (nombre, apellido, cargo, fecha_ingreso)
            VALUES (%s, %s, %s, %s);
            """, (
            faker.first_name(),
            faker.last_name(),
            faker.random_element(elements=('Ingeniero de Sistemas',
                                            'Técnico de Laboratorio',
                                            'Operador de Maquinaria',
                                            'Supervisor de Planta',
                                            'Gerente de Producción')),
            faker.date_between(start_date="-10y", end_date="today")
        ))

        # Insertar en ConsumoEnergia 10
        consumo_energia_id = insert_data(conn, """
            INSERT INTO ConsumoEnergia (maquina_id, consumo_kwh, costo, fecha)
            VALUES (%s, %s, %s, %s);
            """, (
            maquina_id,
            faker.pydecimal(left_digits=5, right_digits=2, positive=True),  # Corregido para uso correcto
            faker.pydecimal(left_digits=5, right_digits=2, positive=True),  # Corregido para uso correcto
            faker.date_between(start_date="-1y", end_date="today")
        ))

        # Insertar en AsignacionPersonal 11
        asignacion_personal_id = insert_data(conn, """
            INSERT INTO AsignacionPersonal (personal_id, fecha, horas_trabajo, remuneracion)
            VALUES (%s, %s, %s, %s);
            """, (
            personal_id,
            faker.date_between(start_date="-1y", end_date="today"),
            faker.random_int(min=1, max=24),
            faker.pydecimal(left_digits=5, right_digits=2, positive=True)  # Corregido para uso correcto
        ))

        # Insertar en Produccion 12 (asumiendo la existencia de lote_id y fase_id)
        produccion_id = insert_data(conn, """
            INSERT INTO Produccion (fecha, plantas_producidas, lote_id, fase_id)
            VALUES (%s, %s, %s, %s);
            """, (
            faker.date_between(start_date="today", end_date="+1y"),
            faker.random_number(digits=5),  # Asegúrate que este campo pueda manejar grandes enteros
            lote_id,
            fase_id
        ))

        # Insertar en ProduccionInsumos 13 (asumiendo la existencia de medio_id)
        produccion_insumos_id = insert_data(conn, """
            INSERT INTO ProduccionInsumos (produccion_id, medio_id, cantidad_usada)
            VALUES (%s, %s, %s);
            """, (
            produccion_id,
            medio_id,
            faker.pydecimal(left_digits=5, right_digits=2, positive=True)  # Ajuste a decimal
        ))

        # Insertar en ProduccionServicios 14 (asumiendo la existencia de servicio_id)
        servicio_id = 1  # Ejemplo de ID
        insert_data(conn, """
            INSERT INTO ProduccionServicios (produccion_id, servicio_id, consumo_energia_id)
            VALUES (%s, %s, %s);
            """, (
            produccion_id,
            servicio_id,
            consumo_energia_id
        ))

        # Insertar en ProduccionPersonal 15
        insert_data(conn, """
            INSERT INTO ProduccionPersonal (produccion_id, asignacion_personal_id)
            VALUES (%s, %s);
            """, (
            produccion_id,
            asignacion_personal_id
        ))

    # Cerrar la conexión
    conn.close()
else:
    print("No se pudo establecer conexión con la base de datos.")
