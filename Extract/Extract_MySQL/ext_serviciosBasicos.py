from util.db_utils import extraer_datos

def extraer_servicios_basicos():
    query = 'SELECT * FROM ServiciosBasicos'
    datos = extraer_datos(query)
    print(datos)
    return datos