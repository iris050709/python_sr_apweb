from flask import Blueprint, jsonify, request
from controllers.configuracionRiegoController import (
    get_all_configuraciones,
    get_configuracion_by_id,
    create_configuracion,
    update_configuracion,
    delete_configuracion
)

# Creación del Blueprint para configuraciones de riego
configuracion_riego_bp = Blueprint('configuraciones_riego', __name__)

# Obtener todas las configuraciones de riego
@configuracion_riego_bp.route('/', methods=['GET'])
def index():
    configuraciones = get_all_configuraciones()
    return jsonify(configuraciones), 200

# Obtener una configuración de riego por ID
@configuracion_riego_bp.route('/<int:configuracion_id>', methods=['GET'])
def show(configuracion_id):
    configuracion = get_configuracion_by_id(configuracion_id)
    if not configuracion:
        return jsonify({"message": "Configuración no encontrada"}), 404
    return jsonify(configuracion), 200

# Crear una configuración de riego
@configuracion_riego_bp.route('/', methods=['POST'])
def create_config():
    data = request.get_json()

    # Verificar si los datos contienen los campos requeridos
    required_fields = ['usuario_id', 'umbral_humedad', 'horario', 'activo']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Todos los campos son obligatorios"}), 400

    try:
        # Procesa los datos y crea la nueva configuración
        new_config = create_configuracion(data)
        return jsonify(new_config), 201  # Retorna la nueva configuración con un código de éxito
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Retorna error si algo sale mal




# Actualizar una configuración de riego por ID
@configuracion_riego_bp.route('/<int:configuracion_id>', methods=['PUT'])
def update(configuracion_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Datos inválidos o JSON mal formado"}), 400

        required_fields = ['usuario_id', 'umbral_humedad', 'horario', 'activo']
        if not all(field in data for field in required_fields):
            return jsonify({"message": "Todos los campos son obligatorios"}), 400

        configuracion_actualizada = update_configuracion(
            configuracion_id,
            data.get('usuario_id'),
            data.get('umbral_humedad'),
            data.get('horario'),
            bool(data.get('activo'))
        )

        if not configuracion_actualizada:
            return jsonify({"message": "Configuración no encontrada"}), 404

        return jsonify(configuracion_actualizada), 200
    except Exception as e:
        return jsonify({"message": f"Error al actualizar la configuración: {str(e)}"}), 500

# Eliminar una configuración de riego por ID
@configuracion_riego_bp.route('/<int:configuracion_id>', methods=['DELETE'])
def delete(configuracion_id):
    try:
        result = delete_configuracion(configuracion_id)
        if not result:
            return jsonify({"message": "Configuración no encontrada"}), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"message": f"Error al eliminar la configuración: {str(e)}"}), 500
