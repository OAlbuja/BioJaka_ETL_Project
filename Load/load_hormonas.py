import traceback
from util.db_connection import Db_Connection
import pandas as pd

def cargar_medios():
    try:
        #------CONEXION AL STAGING------------
        typeS = 'mysql'
        host = '10.10.10.2' #Direccion host, ejemplo del profe 10.10.10.2
        port = '3306'
        user = 'dwh' #usuario
        pwd = 'elcaro_4Q' #contraseña
        db = 'staging' #Nombre de la base de datos
        con_db_stg = Db_Connection(typeS,host,port,user,pwd,db)
        ses_db_stg = con_db_stg.start()
        if ses_db_stg == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db_stg == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")
        #--------------------------
        sql_stmt = "SELECT store_id, name, city, country FROM tra_hormonas" #MODIFICAR CON LOS PARAMETROS QUE SE NECESITA PARA OBTENER DEL STAGING
        hormonas_tra = pd.read_sql(sql_stmt,ses_db_stg)

        #------CONEXION AL SOR------------
        typeS = 'mysql'
        host = '10.10.10.2' #Direccion host, ejemplo del profe 10.10.10.2
        port = '3306'
        user = 'dwh' #usuario
        pwd = 'elcaro_4Q' #contraseña
        db = 'sor' #Nombre de la base de datos
        con_db_sor = Db_Connection(typeS,host,port,user,pwd,db)
        ses_db_sor = con_db_sor.start()
        if ses_db_sor == -1:
            raise Exception("El tipo de base de datos dado no es válido")
        elif ses_db_sor == -2:
            raise Exception("Error tratando de conectarse a la base de datos ")
        #--------------------------
        #Esto está configurado con el ejemplo del profe
        dim_hormonas_dict = {
            "store_bk" : [],
            "name" : [],
            "city" : [],
            "country" : [],
        }

        if not hormonas_tra:
            for bk,nam,city,cou \
                in zip(hormonas_tra['store_id'],hormonas_tra['name'],hormonas_tra['city'],hormonas_tra['country']):
                dim_hormonas_dict['store_bk'].append(bk)
                dim_hormonas_dict['name'].append(nam)
                dim_hormonas_dict['city'].append(city)
                dim_hormonas_dict['country'].append(cou)

        if dim_hormonas_dict['store_bk']:
            df_dim_hormonas = pd.DataFrame(dim_hormonas_dict)
            df_dim_hormonas.to_sql('dim_hormonas', ses_db_sor, if_exists='append', index=False)    

    except:
        traceback.print_exc()
    finally:
        pass