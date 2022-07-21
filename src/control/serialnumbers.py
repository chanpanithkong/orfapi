from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.serialnumbers import tbserialnumbers
from src.models.serialnumberschema import SerialNumberSchema

jwt = JWTManager(app)

class SerialNumbers(Resource):
    @classmethod
    @jwt_required()
    def get(cls,serialnumber):
        try:  
            serialnumbersdata = tbserialnumbers.query.filter_by(serialnumber=serialnumber).first()
            serialnumbers_schema = SerialNumberSchema()
            serialnumbers_data = serialnumbers_schema.dump(serialnumbersdata)
            return {"serialnumbers":serialnumbers_data}
        except Exception as err:
            return {"msg":err} 


class SerialNumbersList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            serialnumbersdata = tbserialnumbers.query.all()
            serialnumbers_schema = SerialNumberSchema(many = True)
            serialnumbers_data = serialnumbers_schema.dump(serialnumbersdata)
            return {"serialnumbers":serialnumbers_data}
        except Exception as err:
            return {"msg":err} 