from flask_restful import Resource


class HelloWorld(Resource):
    """Sample resource docstring
    """

    def get(self):
        return {
            'message': 'Hello world!'
        }
