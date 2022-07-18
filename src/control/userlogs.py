from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.userlogs import tbuserlogs
from src.models.userlogschema import UserLogSchema

jwt = JWTManager(app)

class UserLog(Resource):
    @classmethod
    @jwt_required()
    def get(cls,userlogid):
        try:  
            usserlogdata = tbuserlogs.query.filter_by(userlogid=userlogid).first()
            userlog_schema = UserLogSchema()
            userlog_data = userlog_schema.dump(usserlogdata)
            return {"userlog":userlog_data}
        except Exception as err:
            return {"msg":err} 


class UserLogList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            usserlogdata = tbuserlogs.query.all()
            userlog_schema = UserLogSchema(many = True)
            userlog_data = userlog_schema.dump(usserlogdata)
            return {"userlog":userlog_data}
        except Exception as err:
            return {"msg":err} 