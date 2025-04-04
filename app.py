from flask import Flask, send_from_directory, abort
from config import db, migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint  # Importar Swagger UI
from flask_jwt_extended import JWTManager

# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'HOLAAAAAAA'
jwt = JWTManager(app)

# Configuración de Swagger UI para la API de Usuarios
SWAGGER_URL_USERS = "/api/users/docs"  # URL donde se accede a Swagger de usuarios
API_URL_USERS = "/static/swaggerUSER.yaml"  # Ruta al archivo swagger.yaml de usuarios

swaggerui_users_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL_USERS,  # La URL donde se sirve Swagger UI
    API_URL_USERS,      # Ruta al archivo YAML de Swagger para usuarios
    config={            # Configuración adicional de Swagger UI
        'app_name': "User API"
    }
)

# Configuración de Swagger UI para la API de Sensores
SWAGGER_URL_SENSORES = "/api/sensores/docs"  # URL donde se accede a Swagger de sensores
API_URL_SENSORES = "/static/swaggerIOT.yaml"  # Ruta al archivo swagger.yaml de sensores

swaggerui_sensores_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL_SENSORES,  # La URL donde se sirve Swagger UI
    API_URL_SENSORES,      # Ruta al archivo YAML de Swagger para sensores
    config={               # Configuración adicional de Swagger UI
        'app_name': "Datos Sensores API"
    }
)

# Registrar los blueprints de Swagger
app.register_blueprint(swaggerui_users_blueprint, url_prefix=SWAGGER_URL_USERS)
app.register_blueprint(swaggerui_sensores_blueprint, url_prefix=SWAGGER_URL_SENSORES)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear la carpeta de uploads si no existe
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)

# Rutas de tu aplicación
from routes.user import user_bp
app.register_blueprint(user_bp, url_prefix='/users')

from routes.alertas import alerta_bp
app.register_blueprint(alerta_bp, url_prefix='/alertas')  

from routes.configuracionRiego import configuracion_riego_bp
app.register_blueprint(configuracion_riego_bp, url_prefix='/configuraciones_riego') 

from routes.registroSensor import registro_bp
app.register_blueprint(registro_bp, url_prefix='/registros')  

from routes.riego import riego_bp
app.register_blueprint(riego_bp, url_prefix='/riegos')  

from routes.sensor import sensor_bp
app.register_blueprint(sensor_bp, url_prefix='/sensores')  

from routes.valvula import valvula_bp
app.register_blueprint(valvula_bp, url_prefix='/valvulas')  

from routes.datosSensores import dato_bp
app.register_blueprint(dato_bp, url_prefix='/datos') 

@app.route("/uploads/<filename>")
def get_image(filename):
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    except FileNotFoundError:
        abort(404, description="Imagen no encontrada")

if __name__ == '__main__':
    app.run(debug=True)
