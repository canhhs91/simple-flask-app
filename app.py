# Importing the necessary modules and libraries
from flask import Flask
from flask_migrate import Migrate
from modules.items.routes import blueprint as item_blueprint
from db import db


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database
    with app.app_context():
        db.create_all()
        # Registering the blueprint
        app.register_blueprint(item_blueprint, url_prefix='/items')
    return app


app = create_app()  # Creating the app

migrate = Migrate(app, db)  # Initializing the migration


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)
