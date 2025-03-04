from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from datetime import datetime
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

    # List of required fields
    required_fields = ['nombre', 'correo', 'password', 'rol', 'fecha_nacimiento', 'sexo']

    # Check if all required fields are present
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    # Fetch the user to update
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"message": "Usuario no encontrado"}), 404  # User not found

    # Validate and hash the password if changed
    password_hash = generate_password_hash(data['password'])

    # Parse the date of birth and ensure it's in a valid format
    try:
        fecha_nacimiento = datetime.strptime(data['fecha_nacimiento'], "%Y-%m-%d")
    except ValueError:
        return jsonify({"message": "El formato de la fecha de nacimiento es inválido. Debe ser YYYY-MM-DD."}), 400

    # Update user with the new data
    try:
        updated_user = update_user(
            user_id,
            data['nombre'], 
            data['correo'], 
            password_hash,  # Store hashed password
            data['rol'], 
            data.get('foto'),  # foto can be optional
            fecha_nacimiento,  # Store as a datetime object
            data['sexo']
        )
    except Exception as e:
        return jsonify({"message": f"Error al actualizar el usuario: {str(e)}"}), 500  # Internal server error

    return jsonify(updated_user), 200  # Return updated user data and 200 OK status

# Eliminar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    try:
        result = delete_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar el usuario: {str(e)}"}), 500
