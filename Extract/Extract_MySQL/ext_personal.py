from util.db_utils import extraer_datos

def extraer_personal():
    query = 'SELECT * FROM Personal'
    datos = extraer_datos(query)
    print(datos)
    return datos