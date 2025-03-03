from flask import Blueprint, jsonify, request
from controllers.riegoController import (
    get_all_riegos, get_riego_by_id, create_riego, update_riego, delete_riego
)

riego_bp = Blueprint('riegos', __name__)

# Obtener todos los riegos
@riego_bp.route('/', methods=['GET'])
def index():
    try:
        riegos = get_all_riegos()
        return jsonify(riegos), 200
    except Exception as e:
        return jsonify({"error": f"Error al obtener los riegos: {str(e)}"}), 500

# Obtener un riego por ID
@riego_bp.route('/<int:riego_id>', methods=['GET'])
def show(riego_id):
    riego = get_riego_by_id(riego_id)
    if riego:
        return jsonify(riego), 200
    return jsonify({"error": "Riego no encontrado"}), 404

# Crear un nuevo riego
@riego_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    required_fields = ['valvula_id', 'cantidad_agua', 'duracion']

    # Verificar campos obligatorios
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Faltan los campos: {', '.join(missing_fields)}"}), 400

    # Validaciones de datos
    if not isinstance(data['cantidad_agua'], (int, float)) or data['cantidad_agua'] <= 0:
        return jsonify({"error": "La cantidad de agua debe ser un número positivo"}), 400
    if not isinstance(data['duracion'], (int, float)) or data['duracion'] <= 0:
        return jsonify({"error": "La duración debe ser un número positivo"}), 400

    try:
        nuevo_riego = create_riego(
            data['valvula_id'], data['cantidad_agua'], data['duracion']
        )
        return jsonify(nuevo_riego), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear el riego: {str(e)}"}), 500

# Actualizar un riego por ID
@riego_bp.route('/<int:riego_id>', methods=['PUT'])
def update(riego_id):
    data = request.get_json()
    required_fields = ['valvula_id', 'cantidad_agua', 'duracion']

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Faltan los campos: {', '.join(missing_fields)}"}), 400

    try:
        riego_actualizado = update_riego(
            riego_id, data['valvula_id'], data['cantidad_agua'], data['duracion']
        )
        if riego_actualizado:
            return jsonify(riego_actualizado), 200
        return jsonify({"error": "Riego no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al actualizar el riego: {str(e)}"}), 500

# Eliminar un riego por ID
@riego_bp.route('/<int:riego_id>', methods=['DELETE'])
def delete(riego_id):
    try:
        result = delete_riego(riego_id)
        if result:
            return jsonify({"message": "Riego eliminado exitosamente"}), 200
        return jsonify({"error": "Riego no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": f"Error al eliminar el riego: {str(e)}"}), 500
