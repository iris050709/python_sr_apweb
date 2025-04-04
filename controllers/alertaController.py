from models.Usuario import Usuario
from models.Alerta import Alerta
from flask import request, jsonify
from config import db  

# FUNCION PARA OBTENER ALERTAS
def get_all_alertas():
    try: 
        return [alerta.to_dict() for alerta in Alerta.query.order_by(Alerta.id.desc()).all()]
    except Exception as error:
        print(f"ERROR {error}")
        return []

# FUNCION PARA BUSCAR ALERTA POR ID
def get_alerta_by_id(alerta_id):
    try:
        alerta = Alerta.query.get(alerta_id)
        if alerta:
            return alerta.to_dict()
        else:
            return {"message": "Alerta no encontrada"}, 404
    except Exception as error:
        print(f"ERROR: {error}")
        return {"message": "Error interno"}, 500

# FUNCION PARA CREAR ALERTA
def create_alerta(usuario_id, mensaje):
    try:
        new_alerta = Alerta(usuario_id=usuario_id, mensaje=mensaje)
        db.session.add(new_alerta)
        db.session.commit()
        return new_alerta.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")
        return {"message": "Error al crear la alerta"}, 500

# EDITAR ALERTA POR ID
def update_alerta(alerta_id, usuario_id, mensaje):
    try:
        alerta = Alerta.query.get(alerta_id)
        
        if not alerta:
            return {"message": "Alerta no encontrada"}, 404
        
        alerta.usuario_id = usuario_id
        alerta.mensaje = mensaje
        
        db.session.commit()

        return {
            "message": "Alerta actualizada correctamente",
            "alerta": alerta.to_dict()
        }
    except Exception as e:
        db.session.rollback()  
        return {"message": f"Error al actualizar la alerta: {str(e)}"}, 500

# ELIMINAR ALERTA POR ID
def delete_alerta(alerta_id):
    try:
        alerta = Alerta.query.get(alerta_id)
        if not alerta:
            return {"message": "Alerta no encontrada"}, 404
        
        db.session.delete(alerta)
        db.session.commit()

        return {"message": "Alerta eliminada exitosamente"}
    except Exception as e:
        print(f"ERROR: {e}")
        return {"message": "Error al eliminar la alerta"}, 500
