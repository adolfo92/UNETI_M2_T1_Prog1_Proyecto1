# index.py
from flask import Flask, render_template
import os

# Defino dirección absoluta del directorio de templates
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, "src", "templates")


app = Flask(__name__, template_folder = template_dir)

# decorador para que index.html se ejecuta desde el root de la web
@app.route("/")
def home():
# este es un modulo de flask
	return render_template("index.html")

@app.route("/CremaDeAjoporro")
def receta1():
	return render_template("CremaDeAjoporro.html")

@app.route("/PanDeJamon")
def receta2():
	return render_template("PanDeJamon.html")

@app.route("/PolloHorneado")
def receta3():
	return render_template("PolloHorneado.html")

@app.route("/panArtesanal")
def receta4():
	return render_template("panArtesanal.html")

@app.route("/cervezaGengibre")
def receta5():
	return render_template("/cervezaGengibre.html")

@app.route("/Yogurt")
def receta6():
	return render_template("/Yogurt.html")

if __name__ == "__main__":

	app.run(debug=True, port=4000)