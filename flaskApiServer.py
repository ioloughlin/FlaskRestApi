from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Simple Get with a single parameter.
class HelloWorld(Resource):
    def get(self, cid):
        return {'cid': cid}


api.add_resource(HelloWorld, '/api/customer/<int:cid>')

if __name__ == '__main__':
    app.run(debug=True)