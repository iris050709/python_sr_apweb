from config import db

class RegistroSensor(db.Model):
    __tablename__ = 'registros_sensores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sensor_id = db.Column(db.Integer, nullable=True)  # Puede ser NULL
    valor = db.Column(db.Numeric(5,2), nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "sensor_id": self.sensor_id,
            "valor": float(self.valor),  # Convertir a float para JSON
            "fecha_registro": self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_registro else None
        }
