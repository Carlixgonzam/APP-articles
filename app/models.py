from app import db
from datetime import datetime

class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autores = db.Column(db.String(100), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    palabras_clave = db.Column(db.String(100), nullable=False)
    ruta_pdf = db.Column(db.String(200), nullable=False)
    fecha_agregado = db.Column(db.DateTime, default=datetime.utcnow)
