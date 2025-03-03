from config import db  

class Alerta(db.Model):
    __tablename__ = 'alertas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=True)
    mensaje = db.Column(db.Text, nullable=False)
    fecha_alerta = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "mensaje": self.mensaje,
            "fecha_alerta": self.fecha_alerta.strftime('%Y-%m-%d %H:%M:%S')
        }
