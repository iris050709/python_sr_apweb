from flask import Blueprint, request, jsonify
from controllers.registroSensorController import (
    get_all_registros, get_registro_by_id, create_registro, update_registro, delete_registro
)

# Creación del Blueprint para los registros de sensores
registro_bp = Blueprint('registros', __name__)

# Ruta para obtener todos los registros de sensores
@registro_bp.route('/', methods=['GET'])
def index():
    return get_all_registros()

# Ruta para obtener un registro de sensor por ID
@registro_bp.route('/<int:registro_id>', methods=['GET'])
def show(registro_id):
    return get_registro_by_id(registro_id)

# Ruta para crear un nuevo registro de sensor
@registro_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    
    # Verificar que los datos obligatorios estén presentes
    required_fields = ['sensor_id', 'valor']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    new_registro = create_registro(data['sensor_id'], data['valor'])
    return new_registro

# Ruta para actualizar un registro de sensor por ID
@registro_bp.route('/<int:registro_id>', methods=['PUT'])
def update(registro_id):
    data = request.get_json()
    
    # Verificar que los datos obligatorios estén presentes
    required_fields = ['sensor_id', 'valor']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    updated_registro = update_registro(registro_id, data['sensor_id'], data['valor'])
    return updated_registro

# Ruta para eliminar un registro de sensor por ID
@registro_bp.route('/<int:registro_id>', methods=['DELETE'])
def delete(registro_id):
    return delete_registro(registro_id)
