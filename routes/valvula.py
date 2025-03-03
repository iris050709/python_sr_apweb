from flask import Blueprint, jsonify, request
from controllers.valvulaController import (
    get_all_valvulas, get_valvula_by_id, create_valvula, update_valvula, delete_valvula
)

valvula_bp = Blueprint('valvulas', __name__)

# Obtener todas las válvulas
@valvula_bp.route('/', methods=['GET'])
def index():
    try:
        valvulas = get_all_valvulas()
        return jsonify(valvulas), 200
    except Exception as e:
        return jsonify({"error": f"Error al obtener las válvulas: {str(e)}"}), 500

# Obtener una válvula por ID
@valvula_bp.route('/<int:valvula_id>', methods=['GET'])
def show(valvula_id):
    valvula = get_valvula_by_id(valvula_id)
    if valvula:
        return jsonify(valvula), 200
    return jsonify({"error": "Válvula no encontrada"}), 404

# Crear una nueva válvula
@valvula_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    nombre = data.get('nombre', '').strip()
    ubicacion = data.get('ubicacion')
    estado = data.get('estado', 'Cerrada').capitalize()  # Estado por defecto: "Cerrada"

    # Validaciones
    if not nombre:
        return jsonify({"error": "El nombre es obligatorio"}), 400
    if estado not in ['Abierta', 'Cerrada']:
        return jsonify({"error": "El estado debe ser 'Abierta' o 'Cerrada'"}), 400

    try:
        nueva_valvula = create_valvula(nombre, ubicacion, estado)
        return jsonify(nueva_valvula), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear la válvula: {str(e)}"}), 500

# Actualizar una válvula por ID
@valvula_bp.route('/<int:valvula_id>', methods=['PUT'])
def update(valvula_id):
    data = request.get_json()
    nombre = data.get('nombre', '').strip()
    ubicacion = data.get('ubicacion')
    estado = data.get('estado')

    # Validaciones
    if not nombre:
        return jsonify({"error": "El nombre es obligatorio"}), 400
    if estado and estado not in ['Abierta', 'Cerrada']:
        return jsonify({"error": "El estado debe ser 'Abierta' o 'Cerrada'"}), 400

    try:
        valvula_actualizada = update_valvula(valvula_id, nombre, ubicacion, estado)
        if valvula_actualizada:
            return jsonify(valvula_actualizada), 200
        return jsonify({"error": "Válvula no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al actualizar la válvula: {str(e)}"}), 500

# Eliminar una válvula por ID
@valvula_bp.route('/<int:valvula_id>', methods=['DELETE'])
def delete(valvula_id):
    try:
        result = delete_valvula(valvula_id)
        if result:
            return jsonify({"message": "Válvula eliminada correctamente"}), 200
        return jsonify({"error": "Válvula no encontrada"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al eliminar la válvula: {str(e)}"}), 500
