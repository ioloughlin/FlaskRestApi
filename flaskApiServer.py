from flask import Flask
from flask_restful import Resource, Api
from resources.poc import ProofOfConcept

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
api.add_resource(ProofOfConcept, '/poc', '/poc/<cid>')

# Print Module name
print("Proof of Concept Module name: " + ProofOfConcept.__name__)

if __name__ == '__main__':
    app.run(debug=True)


