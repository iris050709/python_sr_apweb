from models.Usuario import Usuario
from flask import request, jsonify
from config import db  

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

# FUNCION PARA CREAR USUARIO
def create_user(nombre, correo, password, rol, foto, fecha_nacimiento, sexo):
    try:
        existing_user = Usuario.query.filter_by(correo=correo).first()
        if existing_user:
            return {"message": "El correo electrónico ya está registrado"}, 400

        new_user = Usuario(nombre=nombre, correo=correo, password=password, rol=rol, foto=foto, fecha_nacimiento=fecha_nacimiento, sexo=sexo)
        db.session.add(new_user)
        db.session.commit()

        return new_user.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")

# EDITAR USUARIO POR ID
def update_user(user_id, nombre, correo, password, rol, foto, fecha_nacimiento, sexo):
    try:
        user = Usuario.query.get(user_id)
        if not user:
            return jsonify({"message": "Usuario no encontrado"}), 404

        existing_user = Usuario.query.filter_by(correo=correo).first()
        if existing_user and existing_user.id != user_id:
            return jsonify({"message": "El correo electrónico ya está registrado"}), 400

        user.nombre = nombre
        user.correo = correo
        user.password = password
        user.rol = rol
        user.foto = foto
        user.fecha_nacimiento = fecha_nacimiento
        user.sexo = sexo
        
        db.session.commit()
        return user.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")

# ELIMINAR USUARIO POR ID
def delete_user(user_id):
    try:
        user = Usuario.query.get(user_id)
        if not user:
            return {"message": "Usuario no encontrado"}, 404
        
        db.session.delete(user)
        db.session.commit()

        return {"message": "Usuario eliminado exitosamente"}
    except Exception as e:
        print(f"ERROR: {e}")
