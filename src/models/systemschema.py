from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.systems import tbsystems
from ..config.db import db

class SystemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbsystems
        sqla_session = db.session
        load_instance = True

    systemid = auto_field()
    systemname = auto_field()
    details = auto_field()
