from util.db_utils import extraer_datos

def extraer_produccion_insumos():
    query = 'SELECT * FROM ProduccionInsumos'
    datos = extraer_datos(query)
    print(datos)
    return datos