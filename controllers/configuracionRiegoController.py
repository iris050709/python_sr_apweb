from models.ConfiguracionRiego import ConfiguracionRiego
from flask import request, jsonify
from config import db  

# FUNCION PARA OBTENER TODAS LAS CONFIGURACIONES DE RIEGO
def get_all_configuraciones():
    try:
        configuraciones = ConfiguracionRiego.query.order_by(ConfiguracionRiego.id.desc()).all()
        return [config.to_dict() for config in configuraciones]
    except Exception as error:
        print(f"ERROR {error}")
        return []

# FUNCION PARA BUSCAR UNA CONFIGURACIÓN POR ID
def get_configuracion_by_id(config_id):
    try:
        config = ConfiguracionRiego.query.get(config_id)
        if config:
            return config.to_dict()  # Return the dictionary directly
        else:
            return {"message": "Configuración no encontrada"}, 404  # Return data as a dictionary with a 404 status code
    except Exception as error:
        print(f"ERROR: {error}")
        return {"message": "Error al obtener la configuración"}, 500  # Handle the exception and return a 500 error


# FUNCION PARA CREAR UNA CONFIGURACIÓN DE RIEGO
# Función para crear una configuración de riego
def create_configuracion(usuario_id, umbral_humedad, horario, activo):
    if not usuario_id or not umbral_humedad or not horario or activo is None:
        return {"message": "Faltan campos obligatorios."}, 400  # 400 es para solicitud incorrecta

    try:
        # Asegurarse de que 'activo' es 0 o 1, y que se convierte a un Booleano
        if activo not in [0, 1]:
            return {"message": "El valor de 'activo' debe ser 0 o 1."}, 400

        new_config = ConfiguracionRiego(
            usuario_id=usuario_id,
            umbral_humedad=umbral_humedad,
            horario=horario,
            activo=bool(activo)  # Convertimos explícitamente 0 o 1 a False o True
        )
        db.session.add(new_config)
        db.session.commit()

        return new_config.to_dict(), 201  # Configuración creada con éxito

    except Exception as e:
        print(f"ERROR: {e}")
        return {"message": "Error al crear la configuración de riego"}, 500  # Error interno del servidor



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
