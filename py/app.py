from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>¡Hola, Flask está funcionando!</h1><p>Esta es tu primera página web en Python.</p>"

if __name__ == "__main__":
    app.run(debug=True)

