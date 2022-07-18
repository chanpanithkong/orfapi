from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.systemserialnumbers import tbsystemserialnumbers
from src.models.systemserialnumberschema import SystemSerialNumberSchema

jwt = JWTManager(app)

class SystemSertialNumber(Resource):
    @classmethod
    @jwt_required()
    def get(cls,systemid):
        try:  
            systemserialnumberdata = tbsystemserialnumbers.query.filter_by(systemid=systemid).first()
            systemserialnumber_schema = SystemSerialNumberSchema()
            systemserialnumber_data = systemserialnumber_schema.dump(systemserialnumberdata)
            return {"systemsertialnumber":systemserialnumber_data}
        except Exception as err:
            return {"msg":err} 


class SystemSertialNumberList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            systemserialnumberdata = tbsystemserialnumbers.query.all()
            systemserialnumber_schema = SystemSerialNumberSchema(many = True)
            systemserialnumber_data = systemserialnumber_schema.dump(systemserialnumberdata)
            return {"systemsertialnumber":systemserialnumber_data}
        except Exception as err:
            return {"msg":err} 