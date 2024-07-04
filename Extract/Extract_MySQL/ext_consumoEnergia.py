# Archivo: Extract/Extract_OLTP/ext_consumo_energia.py
from util.db_utils import extraer_datos

def extraer_consumo_energia():
    query = 'SELECT * FROM ConsumoEnergia'
    datos = extraer_datos(query)
    print(datos)  # Imprimir los datos en la consola
    return datos
