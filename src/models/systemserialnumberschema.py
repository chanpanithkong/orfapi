from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.systemserialnumbers import tbsystemserialnumbers
from ..config.db import db

class SystemSerialNumberSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbsystemserialnumbers
        sqla_session = db.session
        load_instance = True

    systemid = auto_field()
    sertailnumber = auto_field()
    status = auto_field()
    details = auto_field()
