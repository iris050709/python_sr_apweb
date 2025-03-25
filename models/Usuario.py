from config import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('Administrador', 'Usuario', 'Sistema'), nullable=False)
    foto = db.Column(db.String(255), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.Enum('Masculino', 'Femenino', 'Otro'), nullable=False)
    fecha_registro = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    resetCode = db.Column(db.String(6), nullable=True)
    resetCodeExpiration = db.Column(db.DateTime, nullable=True)

    def check_password (self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "correo": self.correo,
            "rol": self.rol,
            "foto": f"/uploads/{self.foto}" if self.foto else None,
            "fecha_nacimiento": str(self.fecha_nacimiento),
            "sexo": self.sexo,
            "fecha_registro": str(self.fecha_registro),
        }
