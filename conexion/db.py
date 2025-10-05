import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",        # Cambia esto si tu base de datos está en otro servidor
            database="estudiantes",  # Nombre de la base de datos en HeidiSQL
            user="root",             # Tu usuario de MySQL
            password="themago30"
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None
