from config import db

class Sensor(db.Model):
    __tablename__ = 'sensores'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.Enum('Humedad', 'Temperatura'), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=True)
    fecha_instalacion = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "ubicacion": self.ubicacion,
            "fecha_instalacion": self.fecha_instalacion.strftime('%Y-%m-%d %H:%M:%S')
        }
