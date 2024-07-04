import traceback
from util.db_connection import Db_Connection
import pandas as pd
 
def transformar_resumen_produccion_lote():
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
            p.id AS produccion_id,
            l.codigo AS lote_codigo,
            l.planta AS planta,
            f.nombre AS fase,
            pr.nombre AS proceso,
            p.fecha AS fecha_produccion,
            p.plantas_producidas AS plantas_producidas,
            SUM(pi.cantidad_usada * COALESCE(m.costo, 0)) AS costo_total_insumos_medios,
            SUM(pi.cantidad_usada * COALESCE(h.costo, 0)) AS costo_total_insumos_hormonas,
            SUM(pi.cantidad_usada * COALESCE(r.costo, 0)) AS costo_total_insumos_reactivos,
            SUM(sb.costo) AS costo_servicios,
            SUM(ap.remuneracion) AS costo_personal
        FROM 
            ext_produccion p
            JOIN ext_lotes l ON p.lote_id = l.id
            JOIN ext_fases f ON p.fase_id = f.id
            JOIN ext_procesos pr ON f.proceso_id = pr.id
            LEFT JOIN ext_produccion_insumos pi ON p.id = pi.produccion_id
            LEFT JOIN ext_medios m ON pi.medio_id = m.id
            LEFT JOIN ext_hormonas h ON pi.medio_id = h.id
            LEFT JOIN ext_reactivos r ON pi.medio_id = r.id
            LEFT JOIN ext_produccion_servicios ps ON p.id = ps.produccion_id
            LEFT JOIN ext_servicios_basicos sb ON ps.servicio_id = sb.id
            LEFT JOIN ext_produccion_personal pp ON p.id = pp.produccion_id
            LEFT JOIN ext_asignacionPersonal ap ON pp.asignacion_personal_id = ap.id
        GROUP BY 
            p.id, l.codigo, l.planta, f.nombre, pr.nombre, p.fecha, p.plantas_producidas;
        """
        tra_resumen_produccion_lote = pd.read_sql(sql_stmt, ses_db)
        return tra_resumen_produccion_lote
    except:
        traceback.print_exc()
    finally:
        pass

# Guardar en staging
def guardar_resumen_produccion_lote(datos):
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
        # Guardar los datos transformados en la tabla de resumen
        datos.to_sql('tra_ResumenProduccionLote', con=ses_db, if_exists='replace', index=False)
    except:
        traceback.print_exc()
    finally:
        pass
