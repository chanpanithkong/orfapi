from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.serialnumbers import tbserialnumbers
from ..config.db import db

class SerialNumberSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbserialnumbers
        sqla_session = db.session
        load_instance = True

    serialnumber = auto_field()
    formname = auto_field()
    details = auto_field()
