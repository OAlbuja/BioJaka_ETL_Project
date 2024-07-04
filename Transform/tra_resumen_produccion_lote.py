import traceback
import pandas as pd
from util.db_connection import Db_Connection

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
        
        # Transformación de los datos
        sql_stmt = """
        SELECT 
            p.id AS produccion_id,
            t.tiempo_id,
            m.maquina_id,
            ap.personal_id,
            f.fase_id,
            pr.proceso_id,
            pi.medio_id AS insumo_id,  -- Considerando que un insumo_id puede ser un medio, hormona o reactivo
            l.codigo AS lote_codigo,
            l.planta,
            p.plantas_producidas,
            ce.consumo_kwh,
            SUM(pi.cantidad_usada * COALESCE(i.costo, 0)) AS costo_total_insumos,
            SUM(sb.costo) AS costo_servicios,
            SUM(ap.remuneracion) AS costo_personal
        FROM 
            ext_produccion p
            JOIN ext_lotes l ON p.lote_id = l.id
            JOIN ext_fases f ON p.fase_id = f.id
            JOIN ext_procesos pr ON f.proceso_id = pr.id
            JOIN ext_produccion_insumos pi ON p.id = pi.produccion_id
            JOIN Dim_Insumos i ON pi.medio_id = i.insumo_id
            JOIN ext_consumoEnergia ce ON p.id = ce.produccion_id
            LEFT JOIN ext_produccion_servicios ps ON p.id = ps.produccion_id
            LEFT JOIN ext_servicios_basicos sb ON ps.servicio_id = sb.id
            LEFT JOIN ext_produccion_personal pp ON p.id = pp.produccion_id
            LEFT JOIN ext_asignacionPersonal ap ON pp.asignacion_personal_id = ap.id
            LEFT JOIN Dim_Tiempo t ON DATE(p.fecha) = t.fecha
        GROUP BY 
            p.id, t.tiempo_id, m.maquina_id, ap.personal_id, f.fase_id, pr.proceso_id, pi.medio_id, l.codigo, l.planta, p.plantas_producidas, ce.consumo_kwh;
        """
        tra_resumen_produccion_lote = pd.read_sql(sql_stmt, ses_db)
        
        # Conexión a la base de datos dimensional
        db = 'sor'
        con_db = Db_Connection(typeS, host, port, user, pwd, db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")

        # Guardar los datos transformados en la tabla de hechos
        tra_resumen_produccion_lote.to_sql('Fact_ProduccionConsumo', con=ses_db, if_exists='replace', index=False)
        
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
