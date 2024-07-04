# Archivo: Extract/Extract_OLTP/ext_asignacion_personal.py
from util.db_utils import extraer_datos

def extraer_asignacion_personal():
    query = 'SELECT * FROM AsignacionPersonal'
    datos = extraer_datos(query)
    print(datos)  # Imprimir los datos en la consola
    return datos
