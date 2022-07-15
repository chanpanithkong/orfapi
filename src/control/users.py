

import string
from flask_restful import Resource

from src.models.users import tbusers

from src.models.userschema import UserSchema

class UserList(Resource):
    @classmethod
    def get(cls):
        try:
            get_usersdata = tbusers.query.all()
            user_schema = UserSchema(many=True)
            user_data = user_schema.dump(get_usersdata)
            return {"users":user_data}
        except Exception as err:
            return {"msg":err} 

class Users(Resource):
    @classmethod
    def get(cls,userid):
        try:  
            get_usersdata = tbusers.find_by_userid(userid)
            user_schema = UserSchema()
            user_data = user_schema.dump(get_usersdata)
            return {"users":user_data}
        except Exception as err:
            return {"msg":err} 