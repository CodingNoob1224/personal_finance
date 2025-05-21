from flask import Flask
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['DB_CONFIG'] = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Pattywu20031224',
        'database': 'finance_db'
    }

    from .routes import main
    app.register_blueprint(main)

    return app
