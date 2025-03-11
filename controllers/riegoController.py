from models.Riego import Riego
from flask import request, jsonify
from config import db  
from datetime import datetime


# FUNCION PARA OBTENER TODOS LOS REGISTROS DE RIEGO
def get_all_riegos():
    try: 
        riegos = Riego.query.all()
        return [riego.to_dict() for riego in riegos]
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"error": "No se pudieron obtener los riegos"}), 500

# FUNCION PARA BUSCAR UN RIEGO POR ID
def get_riego_by_id(riego_id):
    try:
        riego = Riego.query.get(riego_id)
        if riego:
            return riego.to_dict()  # Elimina `jsonify()`
        else:
            return {"message": "Riego no encontrado"}, 404
    except Exception as error:
        print(f"ERROR: {error}")
        return {"error": "Error al buscar riego"}, 500


# FUNCION PARA CREAR UN REGISTRO DE RIEGO
def create_riego(valvula_id, cantidad_agua, duracion, fecha_riego=None):
    try:
        if not fecha_riego:
            fecha_riego = datetime.now()  # Asignar la fecha y hora actuales si no se proporciona
        new_riego = Riego(valvula_id=valvula_id, cantidad_agua=cantidad_agua, duracion=duracion, fecha_riego=fecha_riego)
        db.session.add(new_riego)
        db.session.commit()
        return new_riego.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"error": "Error al crear riego"}), 500

# FUNCION PARA EDITAR UN RIEGO POR ID
def update_riego(riego_id, valvula_id, cantidad_agua, duracion):
    try:
        riego = Riego.query.get(riego_id)
        if not riego:
            return jsonify({"message": "Riego no encontrado"}), 404

        riego.valvula_id = valvula_id
        riego.cantidad_agua = cantidad_agua
        riego.duracion = duracion
        
        db.session.commit()
        return riego.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"error": "Error al actualizar riego"}), 500

# FUNCION PARA ELIMINAR UN RIEGO POR ID
def delete_riego(riego_id):
    try:
        riego = Riego.query.get(riego_id)
        if not riego:
            return jsonify({"message": "Riego no encontrado"}), 404
        
        db.session.delete(riego)
        db.session.commit()

        return jsonify({"message": "Riego eliminado exitosamente"})
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"error": "Error al eliminar riego"}), 500
