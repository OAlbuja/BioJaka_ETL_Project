from util.db_utils import extraer_datos

def extraer_produccion_personal():
    query = 'SELECT * FROM ProduccionPersonal'
    datos = extraer_datos(query)
    print(datos)
    return datos