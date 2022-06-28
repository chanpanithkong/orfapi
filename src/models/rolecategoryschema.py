from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.rolecategories import tbrolecategories
from ..config.db import db

class RoleCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbrolecategories
        sqla_session = db.session
        load_instance = True

    rolecategoryid = auto_field()
    rolecategory = auto_field()
    details = auto_field()
