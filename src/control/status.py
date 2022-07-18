from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.status import tbstatus
from src.models.statusschema import StatusSchema

jwt = JWTManager(app)

class Status(Resource):
    @classmethod
    @jwt_required()
    def get(cls,statusid):
        try:  
            statusdata = tbstatus.query.filter_by(statusid=statusid).first()
            status_schema = StatusSchema()
            status_data = status_schema.dump(statusdata)
            return {"status":status_data}
        except Exception as err:
            return {"msg":err} 


class StatusList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            statusdata = tbstatus.query.all()
            status_schema = StatusSchema(many = True)
            status_data = status_schema.dump(statusdata)
            return {"status":status_data}
        except Exception as err:
            return {"msg":err} 