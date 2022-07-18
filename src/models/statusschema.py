from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.status import tbstatus
from ..config.db import db

class SystemSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbstatus
        sqla_session = db.session
        load_instance = True

    statusid = auto_field()
    status = auto_field()
    details = auto_field()