import psycopg2
from psycopg2 import OperationalError
import csv

def insert_tablapais():
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
        cursor = conn.cursor()

        print("Subiendo...")

        # Leer el archivo CSV y insertar los datos
        with open('hotels/app/crear_db/tablacountry1.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # Saltar la cabecera
            for row in reader:
                row = [None if x == '' or x.isspace() else x for x in row]
                try:
                    cursor.execute("""
                        INSERT INTO app_pais (
                            countrycode, 
                            countryname
                        ) VALUES (%s, %s)
                    """,
                    row
                    )
                except Exception as e:
                    print(f"Error al insertar fila: {e}")

                    # Conectarse a PostgreSQL en la nube
                    conn = psycopg2.connect(
                        dbname="app_hotels",
                        user="avnadmin",
                        password="AVNS_lVvSfnZ_z2Bnmfj5ASI",
                        host="pg-ed88bff-srodriguezcabana-914d.h.aivencloud.com",
                        port="23178"
                    )
                    conn.autocommit = True
                    cursor = conn.cursor()

                    with open('hotels/app/crear_db/tablacountry1.csv', 'r') as f:
                        reader = csv.reader(f, delimiter=';')
                        next(reader)  # Saltar la cabecera
                        for row in reader:
                            cursor.execute("""
                                INSERT INTO app_pais (
                                    countrycode, 
                                    countryname
                                ) VALUES (%s, %s)
                            """,
                            row
                            )
        print("Datos insertados correctamente.")

    except Exception as e:
        print(f"Error: {e}")

def insert_city_data():
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

        # Leer el archivo CSV y insertar los datos
        with open('hotels/app/crear_db/tablacities1.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # Saltar la cabecera
            for row in reader:
                cursor.execute("""
                    INSERT INTO app_ciudad (
                        countrycode_id, 
                        citycode,
                        cityname
                    ) VALUES (%s, %s, %s)
                """,
                row
                )
        print("Datos insertados correctamente.")

    except Exception as e:
        print(f"Error: {e}")


def into_tablehotel():
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

        # Crear una tablawith open('Backend\\src\\Resultados_Saber_11_R_Caribe_2015_2022.csv', 'r', encoding='ISO-8859-1') as f:
        print("Subiendo...")

        # Leer el archivo CSV y insertar los datos
        with open('hotels/app/crear_db/hotelestabla1.csv', 'r', encoding='ISO-8859-1') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # Saltar la cabecera
            for row in reader:
                row = [None if x == '' or x.isspace() else x for x in row]
                try:
                    cursor.execute("""
                                    INSERT INTO app_hotel_info (
                                        citycode_id, 
                                        hotelcode, 
                                        hotelname, 
                                        hotelrating,
                                        address, 
                                        attractions, 
                                        faxnumber, 
                                        hotelfacilities, 
                                        map, 
                                        phonenumber,
                                        pincode, 
                                        hotelwebsiteurl
                                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    """,
                                    row
                                )
                except Exception as e:
                    print(f"Error al insertar fila: {e}")
                    # Reconectar y reintentar
                    # Crear un cursor
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
                    cursor.execute("""
                                    INSERT INTO app_hotel_info (
                                        citycode_id, 
                                        hotelcode, 
                                        hotelname, 
                                        hotelrating,
                                        address, 
                                        attractions, 
                                        faxnumber, 
                                        hotelfacilities, 
                                        map, 
                                        phonenumber,
                                        pincode, 
                                        hotelwebsiteurl
                                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    """,
                                    row
                                )
        print("Datos insertados correctamente.")

    except Exception as e:
        print(f"Error: {e}")

#insert_tablapais()
#insert_city_data()
#into_tablehotel()