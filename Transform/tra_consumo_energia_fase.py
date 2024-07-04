import traceback
from util.db_connection import Db_Connection
import pandas as pd

def transformar_consumo_energia_fase():
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
        #--------------------------
        # Transformación de los datos
        sql_stmt = """
        SELECT
            ce.id AS consumo_energia_id,
            m.nombre AS maquina,
            m.modelo AS modelo,
            f.nombre AS fase,
            pr.nombre AS proceso,
            ce.fecha AS fecha_consumo,
            ce.consumo_kwh AS consumo_kwh,
            ce.costo AS costo
        FROM
            ext_consumoEnergia ce
            JOIN ext_maquinas m ON ce.maquina_id = m.id
            JOIN ext_produccion_servicios ps ON ce.id = ps.consumo_energia_id
            JOIN ext_produccion p ON ps.produccion_id = p.id
            JOIN ext_fases f ON p.fase_id = f.id
            JOIN ext_procesos pr ON f.proceso_id = pr.id;
        """
        tra_consumo_energia_fase = pd.read_sql(sql_stmt, ses_db)
       
        return tra_consumo_energia_fase
    except:
        traceback.print_exc()
    finally:
        pass
