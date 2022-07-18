from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.systems import tbsystems
from src.models.statusschema import SystemSchema

jwt = JWTManager(app)

class System(Resource):
    @classmethod
    @jwt_required()
    def get(cls,systemid):
        try:  
            systemdata = tbsystems.query.filter_by(systemid=systemid).first()
            system_schema = SystemSchema()
            system_data = system_schema.dump(systemdata)
            return {"system":system_data}
        except Exception as err:
            return {"msg":err} 


class SystemList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            systemdata = tbsystems.query.all()
            system_schema = SystemSchema(many = True)
            system_data = system_schema.dump(systemdata)
            return {"system":system_data}
        except Exception as err:
            return {"msg":err} 