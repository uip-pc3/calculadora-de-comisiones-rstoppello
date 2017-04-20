from flask import request, flash,  redirect, render_template, url_for
from app import app
import re
app.secret_key = '7018294174'
import time
import csv


@app.route('/calculadora')
def index():
    return render_template('calculadora.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    tiempo=time.strftime("%d/%m/%Y")
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    venta = request.form['venta']
    if nombre == '' or apellido == '' or venta == '':
        return render_template('calculadora.html', err = 'Debe llenar todos los campos', nombre = nombre, apellido = apellido, venta = venta)
    #elif nombre > 30 or apellido > 30 or venta > 10:
     #   return render_template('calculadora.html', err = 'Algunos de los campos son demasiado largos, verifique por favor.', nombre = nombre, apellido = apellido, venta = venta)
    warning = ""
    if int(venta) > 100000:
        comision = float(venta)*0.15;
        #print (comision)
    elif int(venta) > 75000:
        comision = float(venta)*0.10;
        #print (comision)
    elif int(venta) > 50000:
        comision = float(venta)*0.7;
        #print (comision)
    elif int(venta) > 25000:
        comision = float(venta)*0.5;
        #print (comision)
    elif int(venta)==0:
        comision=0
        warning = "El vendedor recibe un llamado de atencion"
    else:
        comision = float(venta)*0.3;
        #print (comision)


    fecha = time.strftime("%d/%m/%Y")
    archivo = open("data.csv", "a")
    archivo_csv = csv.writer(archivo)
    l1 = [apellido, nombre, venta, comision, fecha]
    archivo_csv.writerow(l1)
    print("se ha guardado los datos satisfactoriamente")
    archivo.close()

    return render_template('resultado.html', venta= venta,nombre = nombre, comision = comision, apellido= apellido, warning=warning)