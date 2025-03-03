from config import db
from datetime import datetime

class Riego(db.Model):
    __tablename__ = 'riegos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valvula_id = db.Column(db.Integer, nullable=True)
    cantidad_agua = db.Column(db.Numeric(5,2), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
    fecha_riego = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def to_dict(self):
        fecha_riego = self.fecha_riego

        # Verifica si es una cadena y conviértela a datetime
        if isinstance(fecha_riego, str):
            try:
                fecha_riego = datetime.strptime(fecha_riego, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                fecha_riego = None  # Si el formato es inválido, usa `None`

        return {
            'id': self.id,
            'valvula_id': self.valvula_id,
            'cantidad_agua': str(self.cantidad_agua),
            'duracion': self.duracion,
            'fecha_riego': fecha_riego.strftime('%Y-%m-%d %H:%M:%S') if fecha_riego else None
        }
