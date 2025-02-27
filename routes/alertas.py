from flask import Blueprint, jsonify, request
from controllers.alertaController import get_all_alertas, get_alerta_by_id, create_alerta, update_alerta, delete_alerta
alerta_bp = Blueprint('alertas', __name__)

# Obtener todas las alertas
@alerta_bp.route('/', methods=['GET'])
def index():
    alertas = get_all_alertas()
    return jsonify(alertas)

# Obtener una alerta por ID
@alerta_bp.route('/<int:alerta_id>', methods=['GET'])
def show(alerta_id):
    return get_alerta_by_id(alerta_id)

# Crear una alerta
@alerta_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    usuario_id = data.get('usuario_id')
    mensaje = data.get('mensaje')

    if not mensaje:
        return jsonify({"message": "El mensaje es obligatorio"}), 400

    nueva_alerta = create_alerta(usuario_id, mensaje)
    return jsonify(nueva_alerta)

# Actualizar una alerta por ID
@alerta_bp.route('/<int:alerta_id>', methods=['PUT'])
def update(alerta_id):
    data = request.get_json()
    usuario_id = data.get('usuario_id')
    mensaje = data.get('mensaje')

    if not mensaje:
        return jsonify({"message": "El mensaje es obligatorio"}), 400

    alerta_actualizada = update_alerta(alerta_id, usuario_id, mensaje)
    return jsonify(alerta_actualizada)

# Eliminar una alerta por ID
@alerta_bp.route('/<int:alerta_id>', methods=['DELETE'])
def delete(alerta_id):
    return jsonify(delete_alerta(alerta_id))
