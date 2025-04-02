from config import db

class DatosSensores(db.Model):
    __tablename__ = 'datos_sensores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nivel_temperatura1 = db.Column(db.Float, nullable=True)
    estado_ventilador1 = db.Column(db.String(10), nullable=True)
    nivel_temperatura2 = db.Column(db.Float, nullable=True)
    estado_ventilador2 = db.Column(db.String(10), nullable=True)
    luz = db.Column(db.Integer, nullable=True)
    estado_led = db.Column(db.String(10), nullable=True)
    agua_detectada = db.Column(db.String(10), nullable=True)
    posicion_servo = db.Column(db.Integer, nullable=True)
    humedad_suelo1 = db.Column(db.Integer, nullable=True)
    estado_bomba1 = db.Column(db.String(10), nullable=True)
    estado_bomba2 = db.Column(db.String(10), nullable=True)
    distancia1 = db.Column(db.Float, nullable=True)
    humedad_suelo2 = db.Column(db.Integer, nullable=True)
    estado_bomba3 = db.Column(db.String(10), nullable=True)
    estado_bomba4 = db.Column(db.String(10), nullable=True)
    distancia2 = db.Column(db.Float, nullable=True)
    fecha_registro = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "nivel_temperatura1": self.nivel_temperatura1,
            "estado_ventilador1": self.estado_ventilador1,
            "nivel_temperatura2": self.nivel_temperatura2,
            "estado_ventilador2": self.estado_ventilador2,
            "luz": self.luz,
            "estado_led": self.estado_led,
            "agua_detectada": self.agua_detectada,
            "posicion_servo": self.posicion_servo,
            "humedad_suelo1": self.humedad_suelo1,
            "estado_bomba1": self.estado_bomba1,
            "estado_bomba2": self.estado_bomba2,
            "distancia1": self.distancia1,
            "humedad_suelo2": self.humedad_suelo2,
            "estado_bomba3": self.estado_bomba3,
            "estado_bomba4": self.estado_bomba4,
            "distancia2": self.distancia2,
            "fecha_registro": self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_registro else None
        }
