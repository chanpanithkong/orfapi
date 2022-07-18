from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from sqlalchemy import true
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.positions import tbpositions
from src.models.positionschema import PositionSchema

jwt = JWTManager(app)

class Position(Resource):
    @classmethod
    @jwt_required()
    def get(cls,positionid):
        try:  
            positiondata = tbpositions.query.filter_by(positionid=positionid).first()
            position_schema = PositionSchema()
            position_data = position_schema.dump(positiondata)
            return {"positions":position_data}
        except Exception as err:
            return {"msg":err} 


class PositionList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            positiondata = tbpositions.query.all()
            position_schema = PositionSchema(many = True)
            position_data = position_schema.dump(positiondata)
            return {"positions":position_data}
        except Exception as err:
            return {"msg":err} 