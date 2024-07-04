import os
import traceback
import pandas as pd
from util.db_connection import Db_Connection

def extraer_datos(query):
    try:
        #------CONEXION------------
        typeS = os.getenv('DB_TYPE')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        user = os.getenv('DB_USER')
        pwd = os.getenv('DB_PASSWORD')
        db = 'oltp' #Nombre de la base de datos

        con_db = Db_Connection(typeS, host, port, user, pwd, db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db == -2:
            raise Exception("Error tratando de conectarse a la base de datos")
        #--------------------------
        #Lectura de la base de datos
        datos = pd.read_sql(query, ses_db)
        return datos
    except:
        traceback.print_exc()
    finally:
        pass