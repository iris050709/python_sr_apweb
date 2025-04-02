from flask import Blueprint, request, jsonify
from controllers.datosSensoresController import (
    get_all_datos, get_dato_by_id, create_dato, update_dato, delete_dato
)

# Creación del Blueprint para los registros de sensores
dato_bp = Blueprint('datos', __name__)

# Ruta para obtener todos los registros de sensores
@dato_bp.route('/', methods=['GET'])
def index():
    return get_all_datos()

# Ruta para obtener un registro de sensor por ID
@dato_bp.route('/<int:dato_id>', methods=['GET'])
def show(dato_id):
    return get_dato_by_id(dato_id)

# Ruta para crear un nuevo registro de sensor
@dato_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    
    # Verificar que los datos obligatorios estén presentes
    required_fields = ['nivel_temperatura1', 'estado_ventilador1', 'nivel_temperatura2', 'estado_ventilador2', 
                       'luz', 'estado_led', 'agua_detectada', 'posicion_servo', 'humedad_suelo1', 'estado_bomba1', 
                       'estado_bomba2', 'distancia1', 'humedad_suelo2', 'estado_bomba3', 'estado_bomba4', 'distancia2']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    new_registro = create_dato(
        data['nivel_temperatura1'], data['estado_ventilador1'], data['nivel_temperatura2'], 
        data['estado_ventilador2'], data['luz'], data['estado_led'], data['agua_detectada'], 
        data['posicion_servo'], data['humedad_suelo1'], data['estado_bomba1'], data['estado_bomba2'], 
        data['distancia1'], data['humedad_suelo2'], data['estado_bomba3'], data['estado_bomba4'], 
        data['distancia2']
    )
    return new_registro

# Ruta para actualizar un registro de sensor por ID
@dato_bp.route('/<int:dato_id>', methods=['PUT'])
def update(dato_id):
    data = request.get_json()
    
    # Verificar que los datos obligatorios estén presentes
    required_fields = ['nivel_temperatura1', 'estado_ventilador1', 'nivel_temperatura2', 'estado_ventilador2', 
                       'luz', 'estado_led', 'agua_detectada', 'posicion_servo', 'humedad_suelo1', 'estado_bomba1', 
                       'estado_bomba2', 'distancia1', 'humedad_suelo2', 'estado_bomba3', 'estado_bomba4', 'distancia2']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    updated_registro = update_dato(
        dato_id, data['nivel_temperatura1'], data['estado_ventilador1'], data['nivel_temperatura2'], 
        data['estado_ventilador2'], data['luz'], data['estado_led'], data['agua_detectada'], 
        data['posicion_servo'], data['humedad_suelo1'], data['estado_bomba1'], data['estado_bomba2'], 
        data['distancia1'], data['humedad_suelo2'], data['estado_bomba3'], data['estado_bomba4'], 
        data['distancia2']
    )
    return updated_registro

# Ruta para eliminar un registro de sensor por ID
@dato_bp.route('/<int:dato_id>', methods=['DELETE'])
def delete(dato_id):
    return delete_dato(dato_id)