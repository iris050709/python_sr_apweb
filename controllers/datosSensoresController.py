from flask import jsonify, request
from models.DatosSensores import DatosSensores
from config import db

# FUNCION PARA OBTENER TODOS LOS REGISTROS

def get_all_datos():
    try:
        datos = DatosSensores.query.all()
        return jsonify([dato.to_dict() for dato in datos])
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al obtener los registros"}), 500

# FUNCION PARA OBTENER UN REGISTRO POR ID
def get_dato_by_id(dato_id):
    try:
        dato = DatosSensores.query.get(dato_id)
        if dato:
            return jsonify(dato.to_dict())
        else:
            return jsonify({"message": "Registro no encontrado"}), 404
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al buscar el registro"}), 500

# FUNCION PARA CREAR UN REGISTRO
def create_dato(nivel_temperatura1, estado_ventilador1, nivel_temperatura2, estado_ventilador2, luz, estado_led, agua_detectada, posicion_servo, humedad_suelo1, estado_bomba1, estado_bomba2, distancia1, humedad_suelo2, estado_bomba3, estado_bomba4, distancia2):
    try:
        new_dato = DatosSensores(
            nivel_temperatura1=nivel_temperatura1,
            estado_ventilador1=estado_ventilador1,
            nivel_temperatura2=nivel_temperatura2,
            estado_ventilador2=estado_ventilador2,
            luz=luz,
            estado_led=estado_led,
            agua_detectada=agua_detectada,
            posicion_servo=posicion_servo,
            humedad_suelo1=humedad_suelo1,
            estado_bomba1=estado_bomba1,
            estado_bomba2=estado_bomba2,
            distancia1=distancia1,
            humedad_suelo2=humedad_suelo2,
            estado_bomba3=estado_bomba3,
            estado_bomba4=estado_bomba4,
            distancia2=distancia2
        )
        db.session.add(new_dato)
        db.session.commit()
        return jsonify(new_dato.to_dict()), 201
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al crear el registro"}), 500

# FUNCION PARA ACTUALIZAR UN REGISTRO POR ID
def update_dato(dato_id, nivel_temperatura1, estado_ventilador1, nivel_temperatura2, estado_ventilador2, luz, estado_led, agua_detectada, posicion_servo, humedad_suelo1, estado_bomba1, estado_bomba2, distancia1, humedad_suelo2, estado_bomba3, estado_bomba4, distancia2):
    try:
        dato = DatosSensores.query.get(dato_id)
        if not dato:
            return jsonify({"message": "Registro no encontrado"}), 404

        dato.nivel_temperatura1 = nivel_temperatura1
        dato.estado_ventilador1 = estado_ventilador1
        dato.nivel_temperatura2 = nivel_temperatura2
        dato.estado_ventilador2 = estado_ventilador2
        dato.luz = luz
        dato.estado_led = estado_led
        dato.agua_detectada = agua_detectada
        dato.posicion_servo = posicion_servo
        dato.humedad_suelo1 = humedad_suelo1
        dato.estado_bomba1 = estado_bomba1
        dato.estado_bomba2 = estado_bomba2
        dato.distancia1 = distancia1
        dato.humedad_suelo2 = humedad_suelo2
        dato.estado_bomba3 = estado_bomba3
        dato.estado_bomba4 = estado_bomba4
        dato.distancia2 = distancia2
        
        db.session.commit()
        return jsonify(dato.to_dict())
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al actualizar el registro"}), 500

# FUNCION PARA ELIMINAR UN REGISTRO POR ID
def delete_dato(dato_id):
    try:
        dato = DatosSensores.query.get(dato_id)
        if not dato:
            return jsonify({"message": "Registro no encontrado"}), 404

        db.session.delete(dato)
        db.session.commit()
        return jsonify({"message": "Registro eliminado exitosamente"})
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al eliminar el registro"}), 500
