import traceback
import pandas as pd

# EXTRACT
# MYSQL
# aquí va a ir la extracción de los datos de la base de datos
from Extract.Extract_MySQL.ext_asignacionPersonal import extraer_asignacion_personal
from Extract.Extract_MySQL.ext_consumoEnergia import extraer_consumo_energia
from Extract.Extract_MySQL.ext_fases import extraer_fases
from Extract.Extract_MySQL.ext_lotes import extraer_lotes
from Extract.Extract_MySQL.ext_maquinas import extraer_maquinas
from Extract.Extract_MySQL.ext_medios import extraer_medios
from Extract.Extract_MySQL.ext_personal import extraer_personal
from Extract.Extract_MySQL.ext_procesos import extraer_procesos
from Extract.Extract_MySQL.ext_produccion import extraer_produccion
from Extract.Extract_MySQL.ext_produccionInsumos import extraer_produccion_insumos
from Extract.Extract_MySQL.ext_produccionPersonal import extraer_produccion_personal
from Extract.Extract_MySQL.ext_produccionServicios import extraer_produccion_servicios
from Extract.Extract_MySQL.ext_serviciosBasicos import extraer_servicios_basicos
# CSV
from Extract.Extract_CSV.ext_hormonas import extraer_hormonas
from Extract.Extract_CSV.ext_reactivos import extraer_reactivos

# Persistencia
from Extract.per_staging import persistir_staging

def main():
    try:
        # MYSQL
        # Extraer datos desde OLTP
        print("Extrayendo datos de AsignacionPersonal desde OLTP")
        asignacion_personal = extraer_asignacion_personal()
        print("Extrayendo datos de ConsumoEnergia desde OLTP")
        consumo_energia = extraer_consumo_energia()
        print("Extrayendo datos de Fases desde OLTP")
        fases = extraer_fases()
        print("Extrayendo datos de Lotes desde OLTP")
        lotes = extraer_lotes()
        print("Extrayendo datos de Maquinas desde OLTP")
        maquinas = extraer_maquinas()
        print("Extrayendo datos de Medios desde OLTP")
        medios = extraer_medios()
        print("Extrayendo datos de Personal desde OLTP")
        personal = extraer_personal()
        print("Extrayendo datos de Procesos desde OLTP")
        procesos = extraer_procesos()
        print("Extrayendo datos de Produccion desde OLTP")
        produccion = extraer_produccion()
        print("Extrayendo datos de ProduccionInsumos desde OLTP")
        produccion_insumos = extraer_produccion_insumos()
        print("Extrayendo datos de ProduccionPersonal desde OLTP")
        produccion_personal = extraer_produccion_personal()
        print("Extrayendo datos de ProduccionServicios desde OLTP")
        produccion_servicios = extraer_produccion_servicios()
        print("Extrayendo datos de ServiciosBasicos desde OLTP")
        servicios_basicos = extraer_servicios_basicos()
        
        # Persistir en staging desde OLTP
        print("Persistiendo en Staging datos de AsignacionPersonal")
        persistir_staging(asignacion_personal, 'ext_asignacionPersonal')
        print("Persistiendo en Staging datos de ConsumoEnergia")
        persistir_staging(consumo_energia, 'ext_consumoEnergia')
        print("Persistiendo en Staging datos de Fases")
        persistir_staging(fases, 'ext_fases')
        print("Persistiendo en Staging datos de Lotes")
        persistir_staging(lotes, 'ext_lotes')
        print("Persistiendo en Staging datos de Maquinas")
        persistir_staging(maquinas, 'ext_maquinas')
        print("Persistiendo en Staging datos de Medios")
        persistir_staging(medios, 'ext_medios')
        print("Persistiendo en Staging datos de Personal")
        persistir_staging(personal, 'ext_personal')
        print("Persistiendo en Staging datos de Procesos")
        persistir_staging(procesos, 'ext_procesos')
        print("Persistiendo en Staging datos de Produccion")
        persistir_staging(produccion, 'ext_produccion')
        print("Persistiendo en Staging datos de ProduccionInsumos")
        persistir_staging(produccion_insumos, 'ext_produccion_insumos')
        print("Persistiendo en Staging datos de ProduccionPersonal")
        persistir_staging(produccion_personal, 'ext_produccion_personal')
        print("Persistiendo en Staging datos de ProduccionServicios")
        persistir_staging(produccion_servicios, 'ext_produccion_servicios')
        print("Persistiendo en Staging datos de ServiciosBasicos")
        persistir_staging(servicios_basicos, 'ext_servicios_basicos')
        
        #CSV
        # Extraer datos desde CSVs
        print("Extrayendo datos de hormonas desde CSV")
        hormonas = extraer_hormonas()
        print("Extrayendo datos de reactivos desde CSV")
        reactivos = extraer_reactivos()
        
        # Persistir en staging CSVs
        print("Persistiendo en Staging datos de hormonas")
        persistir_staging(hormonas, 'ext_hormonas')
        print("Persistiendo en Staging datos de reactivos")
        persistir_staging(reactivos, 'ext_reactivos')
        #procesos de transformación de  datos
        #procesos de carga de datos
    except:
        traceback.print_exc()
    finally:
        pass

if __name__ == "__main__":
    main()
