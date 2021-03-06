from flask import Flask

from snakeeyes.blueprints.page import page


def create_app():
    """
    Create Flask application using Flask app factory pattern

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    app.register_blueprint(page)

    return app


if __name__ == "__main__":
    instance = create_app()
    instance.run()
