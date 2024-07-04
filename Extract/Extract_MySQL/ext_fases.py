from util.db_utils import extraer_datos

def extraer_fases():
    query = 'SELECT * FROM Fases'
    datos = extraer_datos(query)
    print(datos)
    return datos
