import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from config import db  
from models.Usuario import Usuario
from flask_jwt_extended import create_access_token

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Asegurar que la carpeta de uploads existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# FUNCION PARA OBTENER USUARIOS
def get_all_users():
    users = Usuario.query.all()
    try: 
        return [user.to_dict() for user in users]
    except Exception as error:
        print(f"ERROR {error}")

# FUNCION PARA BUSCAR USUARIO POR ID
def get_user_by_id(user_id):
    try:
        user = Usuario.query.get(user_id)
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({"message": "Usuario no encontrado"}), 404
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al buscar el usuario"}), 500

def email_exists(correo, user_id=None):
    try:
        query = Usuario.query.filter(Usuario.correo == correo)
        if user_id:
            query = query.filter(Usuario.id != user_id)
        existing_user = query.first()
        if existing_user:
            return {"exists": True, "message": "El correo electrónico ya está registrado."}
        return {"exists": False, "message": "El correo electrónico no está registrado."}
    except Exception as e:
        print(f"ERROR: {e}")
        return {"exists": False, "message": "Error al verificar el correo."}

# FUNCION PARA CREAR USUARIO
def create_user(nombre, correo, password, rol, foto_filename, fecha_nacimiento, sexo):
    try:
        email_check = email_exists(correo)
        if email_check["exists"]:
            return {"message": email_check["message"]}, 400

        new_user = Usuario(
            nombre=nombre,
            correo=correo,
            password=password,
            rol=rol,
            foto=foto_filename,
            fecha_nacimiento=fecha_nacimiento,
            sexo=sexo
        )

        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")
        return {"message": "Error al crear el usuario"}, 500

# EDITAR USUARIO POR ID
def update_user(user_id, nombre, correo, password, rol, fecha_nacimiento, sexo):
    try:
        user = Usuario.query.get(user_id)
        if not user:
            return {"message": "Usuario no encontrado"}, 404

        email_check = email_exists(correo, user_id)
        if email_check["exists"]:
            return {"message": email_check["message"]}, 400

        user.nombre = nombre
        user.correo = correo
        if password:
            user.password = password
        user.rol = rol
        user.fecha_nacimiento = fecha_nacimiento
        user.sexo = sexo

        db.session.commit()
        return user.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")
        return {"message": "Error al actualizar el usuario"}, 500

# ELIMINAR USUARIO POR ID
def delete_user(user_id):
    try:
        user = Usuario.query.get(user_id)
        if not user:
            return {"message": "Usuario no encontrado"}, 404
        
        if user.foto and os.path.exists(user.foto):
            os.remove(user.foto)
        
        db.session.delete(user)
        db.session.commit()
        return {"message": "Usuario eliminado exitosamente"}
    except Exception as e:
        print(f"ERROR: {e}")
        return {"message": "Error al eliminar el usuario"}, 500
    
def login_user(correo, password):
    user = Usuario.query.filter_by(correo=correo).first() 
    
    if user and user.check_password(password):  # Verificar la contraseña
        access_token = create_access_token(identity=user.id)
        return jsonify({
            'access_token': access_token,
            'user': {
                "id": user.id,
                "nombre": user.nombre,
                "correo": user.correo
            }
        }), 200
    
    return jsonify({"msg": "CREDENCIALES INVÁLIDAS"}), 401