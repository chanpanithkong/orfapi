from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.depts import tbdepts
from src.models.deptschema import DeptSchema

jwt = JWTManager(app)

class Department(Resource):
    @classmethod
    @jwt_required()
    def get(cls,deptid):
        try:  
            deptdata = tbdepts.query.filter_by(deptid=deptid).first()
            dept_schema = DeptSchema()
            dept_data = dept_schema.dump(deptdata)
            return {"dept":dept_data}
        except Exception as err:
            return {"msg":err} 


class DepartmentList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            deptdata = tbdepts.query.all()
            dept_schema = DeptSchema(many = True)
            dept_data = dept_schema.dump(deptdata)
            return {"dept":dept_data}
        except Exception as err:
            return {"msg":err} 