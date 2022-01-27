from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS



socketio = SocketIO(cors_allowed_origins="*")

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_object('config')
    cors = CORS(app)

    from .routes import bp
    app.register_blueprint(bp)

    socketio.init_app(app)    
    return app