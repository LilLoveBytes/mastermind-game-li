from flask import Flask
import os


# creates and congigures the flask app
def create_app(testConfig=None):
    app = Flask(__name__, static_folder="../frontend/build",
                template_folder="../frontend/build")
    # __name__ is the name of the current python module
    # static_folder tells flask to server static files 
        # from the frontend/build folder for serving react
    # template_folder sets the HTML template folder to the build folder
    
    # session secret key
    app.secret_key = "super_secret_key"

    # app is in debug mode if the FLASK_ENV environment variable is set to 'development'
    app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'

    if testConfig:
        app.config.update(testConfig)

    from app.models import gameController

    # Blueprints allow you to group certain routes together
    # registering bps means you connect them to the flask app
    from app.routes.gameRoutes import game_bp
    app.register_blueprint(game_bp)

    # decorators  to handle the root path and any other path
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>') 
    # to serve the react app 
    def serve_react(path):
        # checks if the requested path exists in the static folder
        # if it does, it returns the file from the static folder
        # if it doesn't, it returns the index.html file
        if path and os.path.exists(app.static_folder + '/' + path):
            return app.send_static_file(path)
        return app.send_static_file('index.html')

    return app


if __name__ == "__main__":
    my_app = create_app() # instantiates the app
    my_app.run(debug=False) # runs the app on local server with debug mode off

    # these lines of code aren't necessary when using flask run
    # but when are when using python app/__init__.py
