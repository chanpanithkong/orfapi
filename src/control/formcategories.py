from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from src.config.db import db, app, api
from flask_restful import Resource, request

from src.models.formcategories import tbformcategories
from src.models.formcategoryschema import FormCategorySchema

jwt = JWTManager(app)

class FormCategory(Resource):
    @classmethod
    @jwt_required()
    def get(cls,formcateegoryid):
        try:  
            formcategorydata = tbformcategories.query.filter_by(formcateegoryid=formcateegoryid).first()
            formcategory_schema = FormCategorySchema()
            formcategory_data = formcategory_schema.dump(formcategorydata)
            return {"formcategory":formcategory_data}
        except Exception as err:
            return {"msg":err} 


class FormCategoryList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            formcategorydata = tbformcategories.query.all()
            formcategory_schema = FormCategorySchema(many=True)
            formcategory_data = formcategory_schema.dump(formcategorydata)
            return {"formcategory":formcategory_data}
        except Exception as err:
            return {"msg":err} 