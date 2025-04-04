from models.Valvula import Valvula
from flask import request, jsonify
from config import db

# OBTENER TODAS LAS VÁLVULAS
def get_all_valvulas():
    try:
        # Ordenar por 'id' de manera descendente
        valvulas = Valvula.query.order_by(Valvula.id.desc()).all()
        return [valvula.to_dict() for valvula in valvulas]
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al obtener válvulas"}), 500

# OBTENER UNA VÁLVULA POR ID
def get_valvula_by_id(valvula_id):
    try:
        valvula = Valvula.query.get(valvula_id)
        if valvula:
            return jsonify(valvula.to_dict())
        else:
            return jsonify({"message": "Válvula no encontrada"}), 404
    except Exception as error:
        print(f"ERROR: {error}")
        return jsonify({"message": "Error al obtener la válvula"}), 500

# CREAR UNA NUEVA VÁLVULA
def create_valvula(nombre, ubicacion, estado):
    try:
        nueva_valvula = Valvula(nombre=nombre, ubicacion=ubicacion, estado=estado)
        db.session.add(nueva_valvula)
        db.session.commit()

        return nueva_valvula.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al crear la válvula"}), 500

# ACTUALIZAR UNA VÁLVULA POR ID
def update_valvula(valvula_id, nombre, ubicacion, estado):
    try:
        valvula = Valvula.query.get(valvula_id)
        if not valvula:
            return None

        valvula.nombre = nombre
        valvula.ubicacion = ubicacion
        valvula.estado = estado
        db.session.commit()
        
        return valvula.to_dict()
    except Exception as error:
        print(f"ERROR: {error}")
        db.session.rollback()
        return None


# ELIMINAR UNA VÁLVULA POR ID
def delete_valvula(valvula_id):
    try:
        valvula = Valvula.query.get(valvula_id)
        if not valvula:
            return jsonify({"message": "Válvula no encontrada"}), 404
        
        db.session.delete(valvula)
        db.session.commit()

        return jsonify({"message": "Válvula eliminada exitosamente"})
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "Error al eliminar la válvula"}), 500
