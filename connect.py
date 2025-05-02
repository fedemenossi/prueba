import mysql.connector

db = mysql.connector.connect(
    host="centerbeam.proxy.rlwy.net",                                    
    port=12935,
    user="root",
    password="QbnIpcJeXYYoQYvhnPUjAALwmhmswmmg",
    database="railway"
)

cursor = db.cursor()
cursor.execute("SELECT * from railway.Clietentes")
filas=cursor.fetchall()

for fila in filas:
    print(f"CUIL: {fila[0]} - Nombre: {fila[1]} - Apellido: {fila[2]}")
    
    

