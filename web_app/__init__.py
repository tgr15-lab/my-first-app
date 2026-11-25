from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)