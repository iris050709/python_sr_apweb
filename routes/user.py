import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from controllers.userController import get_all_users, get_user_by_id, create_user, login_user, update_user, delete_user, email_exists

# Creación del Blueprint para usuarios
user_bp = Blueprint('users', __name__)

# Extensiones permitidas para archivos de imagen
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    data = request.form
    required_fields = ['nombre', 'correo', 'password', 'rol', 'fecha_nacimiento', 'sexo']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    # Verificar si el correo ya está registrado
    if email_exists(data['correo'])['exists']:
        return jsonify({"message": "Este correo ya está registrado. Usa otro."}), 400

    # Procesar imagen (foto)
    foto = request.files.get('foto')
    filename = None
    if foto and allowed_file(foto.filename):
        filename = secure_filename(foto.filename)
        upload_folder = current_app.config.get("UPLOAD_FOLDER", "uploads")
        filepath = os.path.join(upload_folder, filename)
        foto.save(filepath)
    elif foto:
        return jsonify({"message": "Formato de imagen no permitido"}), 400

    # Crear usuario en la base de datos
    new_user = create_user(
        nombre=data['nombre'],
        correo=data['correo'],
        password=generate_password_hash(data['password']),
        rol=data['rol'],
        foto_filename=filename,
        fecha_nacimiento=data['fecha_nacimiento'],
        sexo=data['sexo']
    )
    return jsonify(new_user), 201

# Actualizar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['PUT'])
def user_update(user_id):
    data = request.get_json()
    required_fields = ['nombre', 'correo', 'rol', 'fecha_nacimiento', 'sexo']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    user_response = get_user_by_id(user_id)
    if "message" in user_response.json and user_response.json["message"] == "Usuario no encontrado":
        return user_response

    user = user_response.json
    if data['correo'] != user['correo'] and email_exists(data['correo'])['exists']:
        return jsonify({"message": "Este correo ya está en uso por otro usuario."}), 400

    password_hash = user.get("password")
    if 'password' in data and data['password'].strip():
        password_hash = generate_password_hash(data['password'])

    try:
        updated_user = update_user(
            user_id,
            data['nombre'],
            data['correo'],
            password_hash,
            data['rol'],
            data['fecha_nacimiento'],
            data['sexo']
        )
        return jsonify(updated_user), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar el usuario: {str(e)}"}), 500

# Eliminar un usuario por ID
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def user_delete(user_id):
    try:
        result = delete_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar el usuario: {str(e)}"}), 500

# Verificar si un correo ya está registrado
@user_bp.route('/check-email', methods=['POST'])
def check_email():
    data = request.get_json()
    if 'correo' not in data:
        return jsonify({"message": "El campo correo es obligatorio"}), 400
    email_check = email_exists(data['correo'])
    return jsonify(email_check), 200

@user_bp.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    return login_user(data['correo'], data['password'])