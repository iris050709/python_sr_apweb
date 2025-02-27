from flask import Blueprint, jsonify, request
from controllers.riegoController import get_all_riegos, get_riego_by_id, create_riego, update_riego, delete_riego

# Creación del Blueprint para riegos
riego_bp = Blueprint('riegos', __name__)

# Obtener todos los riegos
@riego_bp.route('/', methods=['GET'])
def index():
    riegos = get_all_riegos()
    return jsonify(riegos)

# Obtener un riego por ID
@riego_bp.route('/<int:riego_id>', methods=['GET'])
def show(riego_id):
    return get_riego_by_id(riego_id)

# Crear un nuevo riego
@riego_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    required_fields = ['valvula_id', 'cantidad_agua', 'duracion']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    nuevo_riego = create_riego(
        data['valvula_id'], data['cantidad_agua'], data['duracion']
    )

    return jsonify(nuevo_riego)

# Actualizar un riego por ID
@riego_bp.route('/<int:riego_id>', methods=['PUT'])
def update(riego_id):
    data = request.get_json()
    required_fields = ['valvula_id', 'cantidad_agua', 'duracion']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    riego_actualizado = update_riego(
        riego_id, data['valvula_id'], data['cantidad_agua'], data['duracion']
    )

    return jsonify(riego_actualizado)

# Eliminar un riego por ID
@riego_bp.route('/<int:riego_id>', methods=['DELETE'])
def delete(riego_id):
    try:
        result = delete_riego(riego_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar el riego: {str(e)}"}), 500
