from util.db_utils import extraer_datos

def extraer_lotes():
    query = 'SELECT * FROM Lotes'
    datos = extraer_datos(query)
    print(datos)
    return datos
