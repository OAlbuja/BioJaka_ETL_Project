import traceback
import pandas as pd
from util.db_connection import Db_Connection
from sqlalchemy import text

def cargar_insumos():
    try:
        #------CONEXION AL STAGING------------
        typeS = 'mysql'
        host = '10.10.10.2'
        port = '3306'
        user = 'dwh'
        pwd = 'elcaro_4Q'
        db = 'staging'
        con_db_stg = Db_Connection(typeS, host, port, user, pwd, db)
        ses_db_stg = con_db_stg.start()
        if ses_db_stg == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db_stg == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")
        
        # Extraer datos transformados de staging
        insumos_tra = pd.read_sql("SELECT * FROM tra_insumos", ses_db_stg)

        #------CONEXION AL SOR------------
        db = 'sor'
        con_db_sor = Db_Connection(typeS, host, port, user, pwd, db)
        ses_db_sor = con_db_sor.start()
        if ses_db_sor == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db_sor == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")

        # Cargar los datos transformados en la tabla Dim_Insumos
        insumos_tra.to_sql('Dim_Insumos', con=ses_db_sor, if_exists='replace', index=False)

        # Crear la restricción de clave foránea en Fact_ProduccionConsumo
        with ses_db_sor.connect() as conn:
            conn.execute(text("""
                ALTER TABLE Fact_ProduccionConsumo 
                ADD CONSTRAINT Fact_ProduccionConsumo_ibfk_6 
                FOREIGN KEY (insumo_id) REFERENCES Dim_Insumos(insumo_id)
            """))

    except:
        traceback.print_exc()
    finally:
        pass

if __name__ == "__main__":
    cargar_insumos()
