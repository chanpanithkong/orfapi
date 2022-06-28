from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.users import tbusers
from ..config.db import db

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbusers
        sqla_session = db.session
        load_instance = True

    userid = auto_field()
    password = auto_field()
    firstname = auto_field()
    lastname = auto_field()
    gender = auto_field()
    branchcode = auto_field()
    email = auto_field()
    phonenumber = auto_field()
    address = auto_field()
    deptid = auto_field()
    positionid = auto_field()

