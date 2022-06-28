from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.userrequestforms import tbuserrequestforms
from ..config.db import db

class UserRequestFormSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbuserrequestforms
        sqla_session = db.session
        load_instance = True

    aid = auto_field()
    formid = auto_field()
    formcategoryid = auto_field()
    serialnumber = auto_field()
    fieldname = auto_field()
    fieldvalue = auto_field()
    userid = auto_field()
