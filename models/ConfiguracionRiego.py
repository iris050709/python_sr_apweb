from config import db

class ConfiguracionRiego(db.Model):
    __tablename__ = 'configuraciones_riego'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)  # Relación con usuarios
    umbral_humedad = db.Column(db.Numeric(5, 2), nullable=False)
    horario = db.Column(db.Time, nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=True)

    usuario = db.relationship('Usuario', backref=db.backref('configuraciones', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "umbral_humedad": float(self.umbral_humedad),
            "horario": self.horario.strftime("%H:%M:%S"),  # Se corrigió la coma faltante
            "activo": True if self.activo == 1 else False  # Convierte 1 en True y 0 en False
        }