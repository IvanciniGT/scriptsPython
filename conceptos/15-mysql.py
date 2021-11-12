import mysql.connector
import os

conexion=mysql.connector.connect(
    host="172.18.0.3",
    port=3306,
    user=os.environ.get("DB_USER"),
    password="password",
    database="curso"
)

cursor=conexion.cursor()

respuesta=cursor.execute("SHOW TABLES")

print("TABLAS " +str(respuesta))
cursor.reset()
cursor.execute("DROP TABLE IF EXISTS prueba")
cursor.execute("CREATE TABLE prueba (id INT, descripcion VARCHAR(200))")

respuesta=cursor.execute("SHOW TABLES")
print("TABLAS " +str(respuesta))
cursor.reset()

cursor.execute("INSERT INTO prueba (id, descripcion) VALUES (1,'Primer dato')")
cursor.execute("INSERT INTO prueba (id, descripcion) VALUES (2,'Segundo dato')")

cursor.execute("SELECT * FROM prueba")
filas=cursor.fetchall()
for fila in filas:
    print("FILA "+str(fila))

