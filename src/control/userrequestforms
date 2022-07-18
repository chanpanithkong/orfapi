from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.userrequestforms import tbuserrequestforms
from src.models.userrequestformschema import UserRequestFormSchema

jwt = JWTManager(app)

class UserRequestForm(Resource):
    @classmethod
    @jwt_required()
    def get(cls,aid):
        try:  
            userrequestformdata = tbuserrequestforms.query.filter_by(aid=aid).first()
            userrequestform_schema = UserRequestFormSchema()
            userrequestformdata_data = userrequestform_schema.dump(userrequestformdata)
            return {"userrequestformdata":userrequestformdata_data}
        except Exception as err:
            return {"msg":err} 


class UserRequestFormList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            userrequestformdata = tbuserrequestforms.query.all()
            userrequestform_schema = UserRequestFormSchema(many = True)
            userrequestformdata_data = userrequestform_schema.dump(userrequestformdata)
            return {"userrequestformdata":userrequestformdata_data}
        except Exception as err:
            return {"msg":err} 