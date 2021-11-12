import mysql.connector

conexion=mysql.connector.connect(
    host="172.18.0.3",
    port=3306,
    user="usuario",
    password="password",
    database="curso"
)

cursor=conexion.cursor()

respuesta=cursor.execute("SHOW TABLES")

print("TABLAS " +str(respuesta))
cursor.reset()
cursor.execute("DROP TABLE prueba")
cursor.execute("CREATE TABLE prueba (id INT, descripcion VARCHAR(200))")

respuesta=cursor.execute("SHOW TABLES")
cursor.reset()
print("TABLAS " +str(respuesta))

cursor.execute("INSERT INTO prueba (id, descripcion) VALUES (1,'Primer dato')")
cursor.execute("INSERT INTO prueba (id, descripcion) VALUES (2,'Segundo dato')")

cursor.execute("SELECT * FROM prueba")
filas=cursor.fetchall()
for fila in filas:
    print("FILA "+str(fila))

