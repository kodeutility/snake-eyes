from flask import Flask


def create_app():
    """
    Create Flask application using Flask app factory pattern

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        """
        Render Hello World in browser

        :return: Flask Response
        """
        return "Hello World"

    return app


if __name__ == "__main__":
    instance = create_app()
    instance.run()
