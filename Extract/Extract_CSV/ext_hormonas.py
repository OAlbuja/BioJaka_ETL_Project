#ARCHIVO CSV
import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_hormonas():
    try:
        filename = r'CSVs\hormonas.csv'
        hormonas = pd.read_csv(filename)
        return hormonas
    except:
        traceback.print_exc()
    finally:
        pass