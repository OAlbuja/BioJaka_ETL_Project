import traceback
import pandas as pd
import os
from util.db_connection import Db_Connection

def persistir_staging(df_stg, tab_name):
    try:
        #------CONEXION------------
        typeS = os.getenv('DB_TYPE')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        user = os.getenv('DB_USER')
        pwd = os.getenv('DB_PASSWORD')
        db = os.getenv('DB_NAME')
        
        con_db = Db_Connection(typeS, host, port, user, pwd, db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db == -2:
            raise Exception("Error tratando de conectarse a la base de datos")
        #--------------------------
        #Lectura de la base de datos
        df_stg.to_sql(tab_name, ses_db, if_exists='replace', index=False)
        
    except:
        traceback.print_exc()
    finally:
        pass
