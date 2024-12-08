from flask import Flask
import os


def create_app(testConfig=None):
    app = Flask(__name__)

    app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'

    from app.models import gameController

    from app.gameRoutes import game_bp
    app.register_blueprint(game_bp)

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
