from config import db

class Valvula(db.Model):
    __tablename__ = 'valvulas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.Enum('Abierta', 'Cerrada'), default='Cerrada', nullable=True)
    fecha_instalacion = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "estado": self.estado,
            "fecha_instalacion": self.fecha_instalacion.strftime('%Y-%m-%d %H:%M:%S')
        }
