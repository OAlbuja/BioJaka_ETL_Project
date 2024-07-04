from util.db_utils import extraer_datos

def extraer_produccion():
    query = 'SELECT * FROM Produccion'
    datos = extraer_datos(query)
    print(datos)
    return datos