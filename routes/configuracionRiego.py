from flask import Blueprint, jsonify, request
from controllers.configuracionRiegoController import get_all_configuraciones, get_configuracion_by_id, create_configuracion, update_configuracion, delete_configuracion

# Creación del Blueprint para configuraciones de riego
configuracion_riego_bp = Blueprint('configuraciones_riego', __name__)

# Obtener todas las configuraciones de riego
@configuracion_riego_bp.route('/', methods=['GET'])
def index():
    configuraciones = get_all_configuraciones()
    return jsonify(configuraciones)

# Obtener una configuración de riego por ID
@configuracion_riego_bp.route('/<int:configuracion_id>', methods=['GET'])
def show(configuracion_id):
    return get_configuracion_by_id(configuracion_id)

# Crear una configuración de riego
@configuracion_riego_bp.route('/', methods=['POST'])
def store():
    data = request.get_json()
    required_fields = ['usuario_id', 'umbral_humedad', 'horario', 'activo']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    nueva_configuracion = create_configuracion(
        data['usuario_id'], data['umbral_humedad'], data['horario'], data['activo']
    )

    return jsonify(nueva_configuracion)

# Actualizar una configuración de riego por ID
@configuracion_riego_bp.route('/<int:configuracion_id>', methods=['PUT'])
def update(configuracion_id):
    data = request.get_json()
    required_fields = ['usuario_id', 'umbral_humedad', 'horario', 'activo']

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    configuracion_actualizada = update_configuracion(
        configuracion_id, data['usuario_id'], data['umbral_humedad'], data['horario'], data['activo']
    )

    return jsonify(configuracion_actualizada)

# Eliminar una configuración de riego por ID
@configuracion_riego_bp.route('/<int:configuracion_id>', methods=['DELETE'])
def delete(configuracion_id):
    try:
        result = delete_configuracion(configuracion_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar la configuración: {str(e)}"}), 500
