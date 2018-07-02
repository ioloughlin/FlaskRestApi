from flask_restful import Resource


class PoC(Resource):
    def get(self, cid):
        return {'PoC': cid}
