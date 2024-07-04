from util.db_utils import extraer_datos

def extraer_maquinas():
    query = 'SELECT * FROM Maquinas'
    datos = extraer_datos(query)
    print(datos)
    return datos
