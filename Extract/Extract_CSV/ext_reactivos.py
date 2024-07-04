#ARCHIVO CSV
import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_reactivos():
    try:
        filename = r'CSVs\reactivos.csv'
        reactivos = pd.read_csv(filename)
        return reactivos
    except:
        traceback.print_exc()
    finally:
        pass