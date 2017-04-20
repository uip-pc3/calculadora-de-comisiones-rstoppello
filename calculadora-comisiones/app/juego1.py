from flask import request, redirect, render_template, url_for
from app import app

@app.route('/juego')
def colores():
	return render_template('colores.html')