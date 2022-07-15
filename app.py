from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from marshmallow import ValidationError

from flask_jwt_extended import JWTManager


from blacklist import BLACKLIST
from src.config.db import db, app, api

from src.control.wsusers import WsTokenRefresh, WsUserLogin, WsUserLogout
from src.control.users import UserList, Users

@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return {"msg":err.messages}, 400

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    return jti in BLACKLIST

api.add_resource(WsUserLogin, "/wslogin")
api.add_resource(WsTokenRefresh, "/wsrefresh")
api.add_resource(WsUserLogout, "/wslogout")

api.add_resource(UserList, "/userlist")
api.add_resource(Users, "/userbyid/<userid>")


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
