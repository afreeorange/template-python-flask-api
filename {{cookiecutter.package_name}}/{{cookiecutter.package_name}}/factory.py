from flask import Flask


def create_app(debug=False):
    """{{cookiecutter.package_name}} application factory
    """

    app = Flask(__name__)
    app.debug = debug

    from .service import {{cookiecutter.package_name}}_blueprint
    app.register_blueprint({{cookiecutter.package_name}}_blueprint)

    return app
