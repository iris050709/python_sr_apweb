from config import db
from datetime import datetime

class Valvula(db.Model):
    __tablename__ = 'valvulas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.Enum('Abierta', 'Cerrada'), default='Cerrada', nullable=True)
    fecha_instalacion = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def to_dict(self):
        fecha_instalacion = self.fecha_instalacion

        if isinstance(fecha_instalacion, str):
            if fecha_instalacion == "0000-00-00 00:00:00":
                return {
                    "id": self.id,
                    "nombre": self.nombre,
                    "ubicacion": self.ubicacion,
                    "estado": self.estado,
                    "fecha_instalacion": None  # Evita el error devolviendo `None`
                }
            fecha_instalacion = datetime.strptime(fecha_instalacion, "%Y-%m-%d %H:%M:%S")

        return {
            "id": self.id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "estado": self.estado,
            "fecha_instalacion": fecha_instalacion.strftime('%Y-%m-%d %H:%M:%S') if fecha_instalacion else None
        }

