from flask_jwt_extended import (
    jwt_required,
    JWTManager
)
from src.config.db import db, app, api
from flask_restful import Resource, request
from src.models.users import tbusers

from src.models.userschema import UserSchema

jwt = JWTManager(app)

class UserList(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:
            get_usersdata = tbusers.query.all()
            user_schema = UserSchema(many=True)
            user_data = user_schema.dump(get_usersdata)
            return {"userstest":user_data}
        except Exception as err:
            return {"msg":err} 

class UserDelete(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        try:
            
            data = request.get_json()
            userid = data['data']['userid']
            get_statusdata = tbusers.find_by_userid(userid)
            db.session.delete(get_statusdata)
            db.session.commit()
            return {"msg":"deleted user id :" + id}

        except Exception as err:
            return {"msg":err} 

class UserInsert(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        try:
            
            data = request.get_json()
            userid = data['data']['userid']
            get_statusdata = tbusers.find_by_userid(userid)

            get_statusdata.lastname = data['data']['lastname']
            get_statusdata.firstname = data['data']['firstname']
            get_statusdata.gender = data['data']['gender']
            get_statusdata.branchcode = data['data']['branchcode']
            get_statusdata.email = data['data']['email']
            get_statusdata.phonenumber = data['data']['phonenumber']
            get_statusdata.address = data['data']['address']
            get_statusdata.deptid = data['data']['deptid']
            get_statusdata.positionid = data['data']['positionid']
            

            db.session.add(get_statusdata)
            db.session.commit()
            return {"msg":"deleted user id :" + id}

        except Exception as err:
            return {"msg":err} 

class UserUpdate(Resource):
    @classmethod
    @jwt_required()
    def post(cls):
        try:
            
            data = request.get_json()
            userid = data['data']['userid']
            get_statusdata = tbusers.find_by_userid(userid)

            get_statusdata.lastname = data['data']['lastname']
            get_statusdata.firstname = data['data']['firstname']
            get_statusdata.gender = data['data']['gender']
            get_statusdata.branchcode = data['data']['branchcode']
            get_statusdata.email = data['data']['email']
            get_statusdata.phonenumber = data['data']['phonenumber']
            get_statusdata.address = data['data']['address']
            get_statusdata.deptid = data['data']['deptid']
            get_statusdata.positionid = data['data']['positionid']
            

            db.session.add(get_statusdata)
            db.session.commit()
            return {"msg":"deleted user id :" + id}

        except Exception as err:
            return {"msg":err} 


class Users(Resource):
    @classmethod
    @jwt_required()
    def get(cls,userid):
        try:  
            get_usersdata = tbusers.find_by_userid(userid)
            user_schema = UserSchema()
            user_data = user_schema.dump(get_usersdata)
            return {"users":user_data}
        except Exception as err:
            return {"msg":err} 

class UserLogin(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        try:  
            data = request.get_json()
            userid = data['data']['userid']
            password = data['data']['password']
            
            get_usersdata = tbusers.find_by_userid(userid)
            user_schema = UserSchema()
            user_data = user_schema.dump(get_usersdata)

            if user_data.password == password:
                return {"login":True}
            return {"login":False}
            
        except Exception as err:
            return {"msg":err} 