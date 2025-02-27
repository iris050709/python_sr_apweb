from models.ConfiguracionRiego import ConfiguracionRiego
from flask import request, jsonify
from config import db  

# FUNCION PARA OBTENER TODAS LAS CONFIGURACIONES DE RIEGO
def get_all_configuraciones():
    configuraciones = ConfiguracionRiego.query.all()
    try: 
        return [config.to_dict() for config in configuraciones]
    except Exception as error:
        print(f"ERROR {error}")

# FUNCION PARA BUSCAR UNA CONFIGURACIÓN POR ID
def get_configuracion_by_id(config_id):
    try:
        config = ConfiguracionRiego.query.get(config_id)
        if config:
            return jsonify(config.to_dict())
        else:
            return jsonify({"message": "Configuración no encontrada"}), 404
    except Exception as error:
        print(f"ERROR: {error}")

# FUNCION PARA CREAR UNA CONFIGURACIÓN DE RIEGO
def create_configuracion(usuario_id, umbral_humedad, horario, activo):
    try:
        new_config = ConfiguracionRiego(usuario_id=usuario_id, umbral_humedad=umbral_humedad, horario=horario, activo=activo)
        db.session.add(new_config)
        db.session.commit()

        return new_config.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")

# FUNCION PARA EDITAR UNA CONFIGURACIÓN DE RIEGO POR ID
def update_configuracion(config_id, usuario_id, umbral_humedad, horario, activo):
    try:
        config = ConfiguracionRiego.query.get(config_id)
        if not config:
            return jsonify({"message": "Configuración no encontrada"}), 404

        config.usuario_id = usuario_id
        config.umbral_humedad = umbral_humedad
        config.horario = horario
        config.activo = activo
        
        db.session.commit()
        return config.to_dict()
    except Exception as e:
        print(f"ERROR: {e}")

# FUNCION PARA ELIMINAR UNA CONFIGURACIÓN DE RIEGO POR ID
def delete_configuracion(config_id):
    try:
        config = ConfiguracionRiego.query.get(config_id)
        if not config:
            return {"message": "Configuración no encontrada"}, 404
        
        db.session.delete(config)
        db.session.commit()

        return {"message": "Configuración eliminada exitosamente"}
    except Exception as e:
        print(f"ERROR: {e}")
