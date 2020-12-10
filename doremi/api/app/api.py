from flask import Blueprint
from flask_restful import Api
from .resources.init import AppInitResource


app_blueprint = Blueprint("app", __name__, url_prefix="/app")
app_api = Api(app=app_blueprint)

app_api.add_resource(AppInitResource, "/init")
