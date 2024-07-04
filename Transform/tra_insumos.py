import traceback
import pandas as pd
from util.db_connection import Db_Connection

def transformar_insumos():
    try:
        #------CONEXION------------
        typeS = 'mysql'
        host = '10.10.10.2'
        port = '3306'
        user = 'dwh'
        pwd = 'elcaro_4Q'
        db = 'staging'
        con_db = Db_Connection(typeS, host, port, user, pwd, db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")
        
        # Extraer y transformar datos de insumos
        medios = pd.read_sql("SELECT id AS insumo_id, nombre, 'Medio' AS tipo, tipo AS categoria, costo FROM ext_medios", ses_db)
        hormonas = pd.read_sql("SELECT id AS insumo_id, nombre, 'Hormona' AS tipo, tipo AS categoria, costo FROM ext_hormonas", ses_db)
        reactivos = pd.read_sql("SELECT id AS insumo_id, nombre, 'Reactivo' AS tipo, tipo AS categoria, costo FROM ext_reactivos", ses_db)
        
        insumos = pd.concat([medios, hormonas, reactivos], ignore_index=True)
        
        # Persistir en Staging
        insumos.to_sql('tra_insumos', con=ses_db, if_exists='replace', index=False)
        
        return insumos
    except:
        traceback.print_exc()
    finally:
        pass
