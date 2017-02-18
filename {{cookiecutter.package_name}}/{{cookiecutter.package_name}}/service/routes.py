from . import api
from .resources import HelloWorld

# Start mapping routes to your resources here
api.add_resource(HelloWorld, '/')
