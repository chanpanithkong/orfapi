from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.roles import tbroles
from src.models.roleschema import RoleSchema

jwt = JWTManager(app)

class Role(Resource):
    @classmethod
    @jwt_required()
    def get(cls,roleid):
        try:  
            roledata = tbroles.query.filter_by(roleid=roleid).first()
            role_schema = RoleSchema()
            role_data = role_schema.dump(roledata)
            return {"role":role_data}
        except Exception as err:
            return {"msg":err} 


class RoleList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            roledata = tbroles.query.all()
            role_schema = RoleSchema(many = True)
            role_data = role_schema.dump(roledata)
            return {"role":role_data}
        except Exception as err:
            return {"msg":err} 