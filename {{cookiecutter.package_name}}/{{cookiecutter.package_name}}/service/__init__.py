from flask import Blueprint
from flask_restful import Api

{{cookiecutter.package_name}}_blueprint = Blueprint('{{cookiecutter.package_name}}_blueprint', __name__)

api = Api({{cookiecutter.package_name}}_blueprint)

# This will throw a linting error. Adjust pytest.ini accordingly.
from . import routes
