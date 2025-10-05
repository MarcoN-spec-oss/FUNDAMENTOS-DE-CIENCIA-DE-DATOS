from flask import Flask, render_template, request
from conexion.db import conectar

app = Flask(__name__)

# Ruta para mostrar la interfaz
@app.route("/", methods=["GET", "POST"])
def index():
    calificacion = ""
    if request.method == "POST":
        try:
            # Obtener la nota ingresada por el usuario
            nota = float(request.form["nota"])
            nombre_estudiante = request.form["nombre"]
            
            # Validar que la nota esté en el rango de 0 a 20
            if nota < 0 or nota > 20:
                calificacion = "La nota debe estar entre 0 y 20."
            else:
                # Determinar la calificación en base al rango
                if 18 <= nota <= 20:
                    calificacion = "AD"
                elif 14 <= nota < 17:
                    calificacion = "A"
                elif 11 <= nota < 14:
                    calificacion = "B"
                elif 0 <= nota < 11:
                    calificacion = "C"

                # Conectar a la base de datos y guardar la información
                conexion = conectar()
                if conexion:
                    cursor = conexion.cursor()
                    query = "INSERT INTO calificaciones (nombre_estudiante, nota, calificacion) VALUES (%s, %s, %s)"
                    cursor.execute(query, (nombre_estudiante, nota, calificacion))
                    conexion.commit()
                    cursor.close()
                    conexion.close()

        except ValueError:
            calificacion = "Por favor, ingresa una nota válida."

    return render_template("index.html", calificacion=calificacion)

if __name__ == "__main__":
    app.run(debug=True)
