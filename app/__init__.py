from flask import Flask
from app.views import states_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(states_bp)
    return app