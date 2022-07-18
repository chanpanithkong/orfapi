from flask import Flask, jsonify, request,render_template
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from flask_jwt_extended import JWTManager

from blacklist import BLACKLIST
from src.config.db import db, app, api

from src.control.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout
from src.control.users import UserList, Users, UserLogin, UserDelete,UserInsert, UserUpdate 


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return {"msg":err.messages}, 400

jwt = JWTManager(app)

@app.route('/')
def hello_name():
   return render_template('index.html')

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    return jti in BLACKLIST
# jwt token
api.add_resource(WsUserLogin, "/wslogin")
api.add_resource(WsTokenRefresh, "/wsrefresh")
api.add_resource(WsUserLogout, "/wslogout")

# users
api.add_resource(UserList, "/userlist")
api.add_resource(Users, "/userbyid/<userid>")
api.add_resource(UserDelete, "/userdelete")
api.add_resource(UserUpdate, "/userUpdate")
api.add_resource(UserInsert, "/userUpdate")
api.add_resource(UserLogin, "/userlogin")

# brnaches
# api.add_resource(BranchList, "/branchlist")
# api.add_resource(Branches, "/branchbycode/<branchcode>")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
