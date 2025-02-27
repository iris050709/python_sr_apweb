from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__) 
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)
migrate.init_app(app, db)

# Registrar rutas
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

if __name__ == '__main__':
    app.run(debug=True)
