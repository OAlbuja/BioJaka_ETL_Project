from util.db_utils import extraer_datos

def extraer_produccion_servicios():
    query = 'SELECT * FROM ProduccionServicios'
    datos = extraer_datos(query)
    print(datos)
    return datos