from logging import error
from flask import Flask, render_template, request, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        error=True
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        sexo = request.form.get('sexo')
        if nombre=='' or nombre=="" or edad=="" or sexo =="":
            return render_template('registro.html', error=error)
        return redirect("/test/" + nombre + '/'+ edad + '/' + sexo)
    return render_template('registro.html')

@app.route('/test/<nombre>/<edad>/<sexo>', methods=['GET', 'POST'])
def test(nombre,edad,sexo):
    if request.method == 'POST':
        nombre = nombre 
        edad = edad 
        sexo = sexo
        pregunta1 = request.form.get('pregunta1')
        pregunta2 = request.form.get('pregunta2')
        pregunta3 = request.form.get('pregunta3')
        pregunta4 = request.form.get('pregunta4')
        pregunta5 = request.form.get('pregunta5')
        pregunta6 = request.form.get('pregunta6')
        pregunta7 = request.form.get('pregunta7')
        pregunta8 = request.form.get('pregunta8')
        pregunta9 = request.form.get('pregunta9')
        pregunta10 = request.form.get('pregunta10')
        if pregunta2 == 'A':
            pregunta2 = 0
        if pregunta2 =='B':
            pregunta2 = 2
        if pregunta2 == 'C':
            pregunta2 = 4
        if pregunta2 == 'D':
            pregunta2 = 6
        if pregunta3 == 'A':
            pregunta3 = 0
        if pregunta3 =='B':
            pregunta3 = 2
        if pregunta3 == 'C':
            pregunta3 = 4
        if pregunta3 == 'D':
            pregunta3 = 6
        if pregunta4 == 'A':
            pregunta4 = 0
        if pregunta4 =='B':
            pregunta4 = 2
        if pregunta4 == 'C':
            pregunta4 = 4
        if pregunta4 == 'D':
            pregunta4 = 6
        if pregunta5 == 'A':
            pregunta5 = 0
        if pregunta5 =='B':
            pregunta5 = 2
        if pregunta5 == 'C':
            pregunta5 = 4
        if pregunta5 == 'D':
            pregunta5 = 6
        if pregunta6 == 'A':
            pregunta6 = 0
        if pregunta6 =='B':
            pregunta6 = 2
        if pregunta6 == 'C':
            pregunta6 = 4
        if pregunta6 == 'D':
            pregunta6 = 6
        if pregunta7 == 'A':
            pregunta7 = 0
        if pregunta7 =='B':
            pregunta7 = 2
        if pregunta7 == 'C':
            pregunta7 = 4
        if pregunta7 == 'D':
            pregunta7 = 6
        if pregunta8 == 'A':
            pregunta8 = 0
        if pregunta8 =='B':
            pregunta8 = 2
        if pregunta8 == 'C':
            pregunta8 = 4
        if pregunta8 == 'D':
            pregunta8 = 6
        if pregunta9 == 'A':
            pregunta9 = 0
        if pregunta9 =='B':
            pregunta9 = 2
        if pregunta9 == 'C':
            pregunta9 = 4
        if pregunta9 == 'D':
            pregunta9 = 6
        if pregunta10 == 'A':
            pregunta10 = 0
        if pregunta10 =='B':
            pregunta10 = 2
        if pregunta10 == 'C':
            pregunta10 = 4
        if pregunta10 == 'D':
            pregunta10 = 6
        resultado = pregunta2 + pregunta3 + pregunta4 + pregunta5 + pregunta6 + pregunta7 + pregunta8 + pregunta9 + pregunta10
        total = 10 + resultado
        resultado = str(resultado)
        total = str(total)
        print(total)
        print(resultado)
        print(pregunta1)
        return  redirect("/resultados/" + nombre + '/'+ edad + '/' + sexo + '/' + resultado + '/' + pregunta1 + '/' + total)
    return render_template('test.html', nombre = nombre, edad = edad, sexo = sexo)

@app.route('/resultados/<nombre>/<edad>/<sexo>/<resultado>/<pregunta1>/<total>')
def resultados(nombre, edad, sexo,resultado,pregunta1,total):
    nombre = nombre
    edad = edad 
    sexo =sexo
    resultado = resultado
    return render_template('resultados.html', nombre = nombre, edad = edad, sexo = sexo, resultado=resultado,pregunta1=pregunta1,total = total)