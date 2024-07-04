import traceback
from util.db_connection import Db_Connection
import pandas as pd

def transformar_lotes():
    try:
        #------CONEXION------------
        typeS = 'mysql'
        host = '10.10.10.2' #Direccion host, ejemplo del profe 10.10.10.2
        port = '3306'
        user = 'dwh' #usuario
        pwd = 'elcaro_4Q' #contraseña
        db = 'staging' #Nombre de la base de datos
        con_db = Db_Connection(typeS,host,port,user,pwd,db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")
        #--------------------------
        #Transformacion de los datos
        sql_stmt = "SELECT s.store_id, concat('SAKILA Store ', s.store_id) AS name,\
                        ifnull(ci.city, concat('City ', s.store_id)) AS city, \
                        ifnull(co.country, concat('Country ', s.store_id)) AS country\
                        FROM ext_store AS s \
                        LEFT JOIN ext_address AS a ON (s.address_id = a.address_id) \
                        LEFT JOIN ext_city AS ci ON (a.city_id = ci.city_id) \
                        LEFT JOIN ext_country AS co ON (ci.country_id = co.country_id)"  
        #Query para hacer la transformacion usado en el ejemplo del profe
        #----------------------------
        
        tra_lotes = pd.read_sql(sql_stmt, ses_db)
        
        return tra_lotes
    except:
        traceback.print_exc()
    finally:
        pass