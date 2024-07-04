import traceback
from util.db_connection import Db_Connection
import pandas as pd

def transformar_costo_total_produccion():
    try:
        #------CONEXION------------
        typeS = 'mysql'
        host = '10.10.10.2'
        port = '3306'
        user = 'dwh'
        pwd = 'elcaro_4Q'
        db = 'staging'
        con_db = Db_Connection(typeS,host,port,user,pwd,db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")
        #--------------------------
        
        # Query para calcular el costo total de producción por planta
        sql_stmt = """
        SELECT 
            p.id AS produccion_id,
            SUM(pi.cantidad_usada * m.costo) AS costo_insumos,
            SUM(ap.horas_trabajo * ap.remuneracion) AS costo_mano_obra,
            SUM(ps.consumo_energia_id * sb.costo) AS costo_servicios,
            (SUM(pi.cantidad_usada * m.costo) + SUM(ap.horas_trabajo * ap.remuneracion) + SUM(ps.consumo_energia_id * sb.costo)) AS costo_total
        FROM 
            ext_produccion p
        LEFT JOIN 
            ext_produccion_insumos pi ON p.id = pi.produccion_id
        LEFT JOIN 
            ext_medios m ON pi.medio_id = m.id
        LEFT JOIN 
            ext_produccion_personal pp ON p.id = pp.produccion_id
        LEFT JOIN 
            ext_asignacionPersonal ap ON pp.asignacion_personal_id = ap.id
        LEFT JOIN 
            ext_produccion_servicios ps ON p.id = ps.produccion_id
        LEFT JOIN 
            ext_servicios_basicos sb ON ps.servicio_id = sb.id
        GROUP BY 
            p.id
        """

        tra_costo_total_produccion = pd.read_sql(sql_stmt, ses_db)
        
        return tra_costo_total_produccion
    except:
        traceback.print_exc()
    finally:
        pass
