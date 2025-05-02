import mysql.connector

db = mysql.connector.connect(
    host="centerbeam.proxy.rlwy.net",                                    
    port=12935,
    user="root",
    password="QbnIpcJeXYYoQYvhnPUjAALwmhmswmmg",
    database="railway"
)


##mysql -h centerbeam.proxy.rlwy.net -u root -p QbnIpcJeXYYoQYvhnPUjAALwmhmswmmg --port 12935 --protocol=TCP railway


cursor = db.cursor()
cursor.execute("SELECT * from railway.Tabla1")
filas=cursor.fetchall()

for fila in filas:
    print(f"ID: {fila[0]} - Descripción: {fila[1]}")
    
    

