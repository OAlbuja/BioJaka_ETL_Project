from util.db_utils import extraer_datos

def extraer_procesos():
    query = 'SELECT * FROM Procesos'
    datos = extraer_datos(query)
    print(datos)
    return datos