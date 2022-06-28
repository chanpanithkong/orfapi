from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.depts import tbdepts
from ..config.db import db

class DeptSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbdepts
        sqla_session = db.session
        load_instance = True

    deptid = auto_field()
    deptcode = auto_field()
    departments = auto_field()
    
    