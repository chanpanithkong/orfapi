from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.userlogs import tbuserlogs
from ..config.db import db

class UserLogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbuserlogs
        sqla_session = db.session
        load_instance = True

    userlogid = auto_field()
    activity = auto_field()
    createddate = auto_field()
    createdby = auto_field()

