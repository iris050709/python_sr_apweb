from flask import jsonify, request
from models.RegistroSensor import RegistroSensor
from config import db

# FUNCION PARA OBTENER TODOS LOS REGISTROS DE SENSORES
def get_all_registros():
    try:
        registros = RegistroSensor.query.order_by(RegistroSensor.id.desc()).all()
        return jsonify([registro.to_dict() for registro in registros])
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al obtener los registros"}), 500

# FUNCION PARA OBTENER UN REGISTRO POR ID
def get_registro_by_id(registro_id):
    try:
        registro = RegistroSensor.query.get(registro_id)
        if registro:
            return jsonify(registro.to_dict())
        else:
            return jsonify({"message": "Registro no encontrado"}), 404
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al buscar el registro"}), 500

# FUNCION PARA CREAR UN REGISTRO
def create_registro(sensor_id, valor):
    try:
        new_registro = RegistroSensor(sensor_id=sensor_id, valor=valor)
        db.session.add(new_registro)
        db.session.commit()
        return jsonify(new_registro.to_dict()), 201
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al crear el registro"}), 500

# FUNCION PARA ACTUALIZAR UN REGISTRO POR ID
def update_registro(registro_id, sensor_id, valor):
    try:
        registro = RegistroSensor.query.get(registro_id)
        if not registro:
            return jsonify({"message": "Registro no encontrado"}), 404

        registro.sensor_id = sensor_id
        registro.valor = valor
        
        db.session.commit()
        return jsonify(registro.to_dict())
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al actualizar el registro"}), 500

# FUNCION PARA ELIMINAR UN REGISTRO POR ID
def delete_registro(registro_id):
    try:
        registro = RegistroSensor.query.get(registro_id)
        if not registro:
            return jsonify({"message": "Registro no encontrado"}), 404

        db.session.delete(registro)
        db.session.commit()
        return jsonify({"message": "Registro eliminado exitosamente"})
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al eliminar el registro"}), 500
