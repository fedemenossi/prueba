from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
        host="centerbeam.proxy.rlwy.net",                                    
        port=12935,
        user="root",
        password="QbnIpcJeXYYoQYvhnPUjAALwmhmswmmg",
        database="railway"
    )

def obtener_datos():
    cursor = db.cursor()
    cursor.execute("SELECT * from railway.Tabla1")
    resultados = cursor.fetchall()
    db.close()
    return resultados


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/tabla1")
def mostrar_tabla():
    datos = obtener_datos()
    return render_template("tabla.html", datos2=datos)



##if __name__ == "__main__":
##    app.run(debug=True)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000,debug=True)

