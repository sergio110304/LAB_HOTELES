import psycopg2
from psycopg2 import OperationalError
import pandas as pd

def create_database():
    try:
        # Conectarse a PostgreSQL en la nube
        conn = psycopg2.connect(
            dbname="defaultdb",
            user="avnadmin",
            password="AVNS_lVvSfnZ_z2Bnmfj5ASI",
            host="pg-ed88bff-srodriguezcabana-914d.h.aivencloud.com",
            port="23178"
        )
        conn.autocommit = True
        # Crear un cursor
        cursor = conn.cursor()
        
        # Crear una nueva base de datos
        cursor.execute("CREATE DATABASE APP_HOTELS;")
        print("Base de datos creada correctamente.")

    except OperationalError as e:
        print(f"Error: {e}")


def ver_tablas():
    try:
        # Conectarse a PostgreSQL en la nube
        conn = psycopg2.connect(
            dbname="app_hotels",
            user="avnadmin",
            password="AVNS_lVvSfnZ_z2Bnmfj5ASI",
            host="pg-ed88bff-srodriguezcabana-914d.h.aivencloud.com",
            port="23178"
        )
        conn.autocommit = True
        # Crear un cursor
        cursor = conn.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)
        for table in cursor.fetchall():
            print(table)
    except OperationalError as e:
        print(e)

def ver_columnas(tabla):
    try:
        # Conectarse a PostgreSQL en la nube
        conn = psycopg2.connect(
            dbname="app_hotels",
            user="avnadmin",
            password="AVNS_lVvSfnZ_z2Bnmfj5ASI",
            host="pg-ed88bff-srodriguezcabana-914d.h.aivencloud.com",
            port="23178"
        )
        conn.autocommit = True
        # Crear un cursor
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = '{tabla}'
        """)
        for column in cursor.fetchall():
            print(column)
    except OperationalError as e:
        print(e)

def do_query(query):
    try:
        # Crear un cursor
        conn = psycopg2.connect(
                dbname="app_hotels",
                user="avnadmin",
                password="AVNS_lVvSfnZ_z2Bnmfj5ASI",
                host="pg-ed88bff-srodriguezcabana-914d.h.aivencloud.com",
                port="23178"
            )
        conn.autocommit = True
        cursor = conn.cursor()

        df_resultados = pd.read_sql_query(query, conn)
        
        cursor.close()
        print(df_resultados)
        
    except Exception as e:
        print(f"Error: {e}")

def vaciar_tabla(nombre_tabla):
    try:
        conn = psycopg2.connect(
                dbname="app_hotels",
                user="avnadmin",
                password="AVNS_lVvSfnZ_z2Bnmfj5ASI",
                host="pg-ed88bff-srodriguezcabana-914d.h.aivencloud.com",
                port="23178"
            )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE app_viaje, app_hotel_info;")
        conn.commit()
        print(f"Tabla {nombre_tabla} vaciada con éxito.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

#create_database()

#ver_tablas()    

#ver_columnas('app_pais')

do_query('SELECT * FROM app_hotel_info;')

#vaciar_tabla('app_hotel_info')




