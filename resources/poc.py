from flask_restful import Resource

# Proof of concept class returning JSON data


class ProofOfConcept(Resource):
    def get(self, cid):
        return [
            {
                'PoC': cid,
                'SomeData': 'data'
            },
            {
                'PoC': cid + '1',
                'SomeData': 'data2'
            }
        ]
