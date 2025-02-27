from flask import Blueprint, jsonify, request
from controllers.valvulaController import (
    get_all_valvulas, get_valvula_by_id, create_valvula, update_valvula, delete_valvula
)

valvula_bp = Blueprint('valvulas', __name__)

# Obtener todas las válvulas
@valvula_bp.route('/', methods=['GET'])
def index():
    valvulas = get_all_valvulas()
    return jsonify(valvulas)

# Obtener una válvula por ID
@valvula_bp.route('/<int:valvula_id>', methods=['GET'])
def show(valvula_id):
    return get_valvula_by_id(valvula_id)

# Crear una nueva válvula
@valvula_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    nombre = data.get('nombre')
    ubicacion = data.get('ubicacion')
    estado = data.get('estado', 'Cerrada')  # Estado por defecto: "Cerrada"

    if not nombre:
        return jsonify({"message": "El nombre es obligatorio"}), 400

    nueva_valvula = create_valvula(nombre, ubicacion, estado)
    return jsonify(nueva_valvula)

# Actualizar una válvula por ID
@valvula_bp.route('/<int:valvula_id>', methods=['PUT'])
def update(valvula_id):
    data = request.get_json()
    nombre = data.get('nombre')
    ubicacion = data.get('ubicacion')
    estado = data.get('estado')

    if not nombre:
        return jsonify({"message": "El nombre es obligatorio"}), 400

    valvula_actualizada = update_valvula(valvula_id, nombre, ubicacion, estado)
    return jsonify(valvula_actualizada)

# Eliminar una válvula por ID
@valvula_bp.route('/<int:valvula_id>', methods=['DELETE'])
def delete(valvula_id):
    return delete_valvula(valvula_id)
