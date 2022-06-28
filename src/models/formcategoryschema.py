from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from ..models.formcategories import tbformcategories
from ..config.db import db

class FormCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = tbformcategories
        sqla_session = db.session
        load_instance = True

    formcategoryid = auto_field()
    formcategory = auto_field()
    details = auto_field()
