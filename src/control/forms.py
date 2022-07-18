from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.forms import tbforms
from src.models.formschema import FormSchema

jwt = JWTManager(app)

class Form(Resource):
    @classmethod
    @jwt_required()
    def get(cls,formid):
        try:  
            formdata = tbforms.query.filter_by(formid=formid).first()
            form_schema = FormSchema()
            form_data = form_schema.dump(formdata)
            return {"forms":form_data}
        except Exception as err:
            return {"msg":err} 


class FormList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            formdata = tbforms.query.all()
            form_schema = FormSchema(many = True)
            form_data = form_schema.dump(formdata)
            return {"forms":form_data}
        except Exception as err:
            return {"msg":err} 