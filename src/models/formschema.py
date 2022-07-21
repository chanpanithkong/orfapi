from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.forms import tbforms
from ..config.db import db

class FormSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbforms
        sqla_session = db.session
        load_instance = True

    formid = auto_field()
    formcategoryid = auto_field()
    serialnumber = auto_field()
    fieldname = auto_field()
    fieldcontroller = auto_field()
    status = auto_field()