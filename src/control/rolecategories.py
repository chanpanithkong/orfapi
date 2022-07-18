from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.rolecategories import tbrolecategories
from src.models.rolecategoryschema import RoleCategorySchema

jwt = JWTManager(app)

class RoleCategory(Resource):
    @classmethod
    @jwt_required()
    def get(cls,rolecategoryid):
        try:  
            rolecategorydata = tbrolecategories.query.filter_by(rolecategoryid=rolecategoryid).first()
            rolecategory_schema = RoleCategorySchema()
            rolecategory_data = rolecategory_schema.dump(rolecategorydata)
            return {"rolecategory":rolecategory_data}
        except Exception as err:
            return {"msg":err} 


class RoleCategoryList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            rolecategorydata = tbrolecategories.query.all()
            rolecategory_schema = RoleCategorySchema(many = True)
            rolecategory_data = rolecategory_schema.dump(rolecategorydata)
            return {"rolecategory":rolecategory_data}
        except Exception as err:
            return {"msg":err} 