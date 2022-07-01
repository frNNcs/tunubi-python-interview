from flask import Flask

from apps.views import polls_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(polls_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
