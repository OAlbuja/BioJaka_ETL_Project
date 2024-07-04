from util.db_utils import extraer_datos

def extraer_medios():
    query = 'SELECT * FROM Medios'
    datos = extraer_datos(query)
    print(datos)
    return datos
