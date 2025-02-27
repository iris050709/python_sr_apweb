from config import db

class Riego(db.Model):
    __tablename__ = 'riegos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valvula_id = db.Column(db.Integer, nullable=True)  # Puede ser NULL
    cantidad_agua = db.Column(db.Numeric(5,2), nullable=False)
    duracion = db.Column(db.Integer, nullable=False)
    fecha_riego = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'valvula_id': self.valvula_id,
            'cantidad_agua': str(self.cantidad_agua),
            'duracion': self.duracion,
            'fecha_riego': self.fecha_riego.strftime('%Y-%m-%d %H:%M:%S')
        }
