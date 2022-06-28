from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.roles import tbroles
from ..config.db import db

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbroles
        sqla_session = db.session
        load_instance = True

    roleid = auto_field()
    role = auto_field()
    rolecategoryid = auto_field()
    details = auto_field()