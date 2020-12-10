from flask_restful import Resource
from doremi.utils import ErrorCode
from doremi.utils import make_response


class AppInitResource(Resource):

    def get(self):
        return make_response(ErrorCode.OK, "hello, world.")
