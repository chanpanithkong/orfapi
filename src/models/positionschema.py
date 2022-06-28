from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.positions import tbpositions
from ..config.db import db

class PositionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbpositions
        sqla_session = db.session
        load_instance = True

    positionid = auto_field()
    position = auto_field()
    details = auto_field()