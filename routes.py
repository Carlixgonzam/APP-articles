from app import app, db
from app.models import Articulo
from flask import render_template, request, redirect, url_for, flash
import shutil
import os

@app.route('/')
def index():
    articulos = Articulo.query.order_by(Articulo.fecha_agregado.desc()).all()
    return render_template('index.html', articulos=articulos)

@app.route('/add', methods=['POST'])
def add_article():
    titulo = request.form['titulo']
    autores = request.form['autores']
    año = request.form['año']
    palabras_clave = request.form['palabras_clave']
    ruta_pdf = request.form['ruta_pdf']
    nuevo_articulo = Articulo(titulo=titulo, autores=autores, año=año, palabras_clave=palabras_clave, ruta_pdf=ruta_pdf)
    try:
        db.session.add(nuevo_articulo)
        db.session.commit()
        flash('Artículo agregado correctamente', 'success')
    except:
        flash('Error al agregar el artículo', 'danger')
    return redirect(url_for('index'))

@app.route('/search', methods=['POST'])
def search_articles():
    busqueda = '%' + request.form['buscar'] + '%'
    articulos = Articulo.query.filter(Articulo.palabras_clave.like(busqueda)).all()
    return render_template('index.html', articulos=articulos)
