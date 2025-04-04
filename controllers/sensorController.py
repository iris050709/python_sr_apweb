from models.Sensor import Sensor
from flask import request, jsonify
from config import db  

# FUNCION PARA OBTENER TODOS LOS SENSORES
def get_all_sensores():
    try:
        sensores = Sensor.query.order_by(Sensor.id.desc()).all()
        return [sensor.to_dict() for sensor in sensores]
    except Exception as error:
        print(f"ERROR: {error}")
        return []

# FUNCION PARA BUSCAR SENSOR POR ID
def get_sensor_by_id(sensor_id):
    try:
        sensor = Sensor.query.get(sensor_id)
        if sensor:
            return jsonify(sensor.to_dict())
        else:
            return jsonify({"message": "Sensor no encontrado"}), 404
    except Exception as error:
        print(f"ERROR: {error}")

# FUNCION PARA CREAR SENSOR
def create_sensor(nombre, tipo, ubicacion=None):
    try:
        new_sensor = Sensor(nombre=nombre, tipo=tipo, ubicacion=ubicacion)
        db.session.add(new_sensor)
        db.session.commit()

        return new_sensor.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")

# FUNCION PARA EDITAR SENSOR POR ID
def update_sensor(sensor_id, nombre, tipo, ubicacion=None):
    try:
        sensor = Sensor.query.get(sensor_id)
        if not sensor:
            return jsonify({"message": "Sensor no encontrado"}), 404

        sensor.nombre = nombre
        sensor.tipo = tipo
        sensor.ubicacion = ubicacion

        db.session.commit()
        return sensor.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")

# FUNCION PARA ELIMINAR SENSOR POR ID
def delete_sensor(sensor_id):
    try:
        sensor = Sensor.query.get(sensor_id)
        if not sensor:
            return {"message": "Sensor no encontrado"}, 404

        db.session.delete(sensor)
        db.session.commit()

        return {"message": "Sensor eliminado exitosamente"}
    except Exception as e:
        print(f"ERROR: {e}")
