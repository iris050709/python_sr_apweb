from flask import Blueprint, jsonify, request
from controllers.sensorController import (
    get_all_sensores, get_sensor_by_id, create_sensor, update_sensor, delete_sensor
)

sensor_bp = Blueprint('sensores', __name__)

# Obtener todos los sensores
@sensor_bp.route('/', methods=['GET'])
def index():
    sensores = get_all_sensores()
    return jsonify(sensores)

# Obtener un sensor por ID
@sensor_bp.route('/<int:sensor_id>', methods=['GET'])
def show(sensor_id):
    return get_sensor_by_id(sensor_id)

# Crear un nuevo sensor
@sensor_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    nombre = data.get('nombre')
    tipo = data.get('tipo')
    ubicacion = data.get('ubicacion')

    if not nombre or not tipo:
        return jsonify({"message": "El nombre y tipo son obligatorios"}), 400

    nuevo_sensor = create_sensor(nombre, tipo, ubicacion)
    return jsonify(nuevo_sensor)

# Actualizar un sensor por ID
@sensor_bp.route('/<int:sensor_id>', methods=['PUT'])
def update(sensor_id):
    data = request.get_json()
    nombre = data.get('nombre')
    tipo = data.get('tipo')
    ubicacion = data.get('ubicacion')

    if not nombre or not tipo:
        return jsonify({"message": "El nombre y tipo son obligatorios"}), 400

    sensor_actualizado = update_sensor(sensor_id, nombre, tipo, ubicacion)
    return jsonify(sensor_actualizado)

# Eliminar un sensor por ID
@sensor_bp.route('/<int:sensor_id>', methods=['DELETE'])
def delete(sensor_id):
    return jsonify(delete_sensor(sensor_id))
