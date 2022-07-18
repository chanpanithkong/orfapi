from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.userroles import tbuserroles
from src.models.userroleschema import UserRoleSchema

jwt = JWTManager(app)

class UserRole(Resource):
    @classmethod
    @jwt_required()
    def get(cls,userid):
        try:  
            userroledata = tbuserroles.query.filter_by(userid=userid).first()
            userrole_schema = UserRoleSchema()
            userrole_data = userrole_schema.dump(userroledata)
            return {"userrole":userrole_data}
        except Exception as err:
            return {"msg":err} 


class UserRoleList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            userroledata = tbuserroles.query.all()
            userrole_schema = UserRoleSchema(many=True)
            userrole_data = userrole_schema.dump(userroledata)
            return {"userrole":userrole_data}
        except Exception as err:
            return {"msg":err} 