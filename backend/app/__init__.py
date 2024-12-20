from flask import Flask
import os



def create_app(testConfig=None):
    app = Flask(__name__, static_folder="../frontend/build",
                template_folder="../frontend/build")
    
    # session secret key
    app.secret_key = "super_secret_key"

    app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'

    if testConfig:
        app.config.update(testConfig)

    from app.models import gameController

    from app.routes.gameRoutes import game_bp
    app.register_blueprint(game_bp)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>') 
    def serve_react(path):
        if path and os.path.exists(app.static_folder + '/' + path):
            return app.send_static_file(path)
        return app.send_static_file('index.html')

    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=False)
