from flask import Blueprint, jsonify, request
from controllers.userController import get_all_users, get_user_by_id, create_user, update_user, delete_user

# Creación del Blueprint para usuarios
user_bp = Blueprint('users', __name__)

# Obtener todos los usuarios
@user_bp.route('/', methods=['GET'])
def index():
    users = get_all_users()
    return jsonify(users)

# Obtener un usuario por ID
@user_bp.route('/<int:user_id>', methods=['GET'])
def show(user_id):
    return get_user_by_id(user_id)

# Crear un usuario
@user_bp.route('/', methods=['POST'])
def user_store():
    data = request.get_json()
    required_fields = ['nombre', 'correo', 'password', 'rol', 'foto', 'fecha_nacimiento', 'sexo']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    new_user = create_user(
        data['nombre'], data['correo'], data['password'], 
        data['rol'], data['foto'], data['fecha_nacimiento'], data['sexo']
    )
    
    return jsonify(new_user)

# Actualizar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    required_fields = ['nombre', 'correo', 'password', 'rol', 'foto', 'fecha_nacimiento', 'sexo']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    updated_user = update_user(
        user_id, data['nombre'], data['correo'], data['password'], 
        data['rol'], data['foto'], data['fecha_nacimiento'], data['sexo']
    )
    
    return jsonify(updated_user)

# Eliminar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    try:
        result = delete_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar el usuario: {str(e)}"}), 500
