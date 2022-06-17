# import logging
# import sys

# from flask import Flask, request, jsonify, make_response, json,Blueprint
# from sqlalchemy import table
# from src.models.status import tbstatus
# from src.models.statusschema import StatusSchema
# from src.config.db import app, db

# from src.api.main import response_with
# import src.api.respond as resp

from flask import Flask, request, jsonify, make_response, json,Blueprint
from src.route import example_blueprint

from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
bp = Blueprint('frontend', __name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)


@swaggerui_blueprint.route('/')
def index():
    return '<h1>Hello World!</h1>'




app.register_blueprint(swaggerui_blueprint)


@app.errorhandler(404)
def not_found(e):
    return "<h1>Not found</h1>"

# @app.route('/status', methods = ['GET'])
# def getStatusList():
   
#     try:

#         get_statusdata = tbstatus.query.all()
#         status_schema = StatusSchema(many=True)
#         status_data = status_schema.dump(get_statusdata)
#         return make_response( jsonify({"status":status_data}) )
#     except Exception as e:
#         logging.error(e)
#         return response_with(resp.INVALID_INPUT_422)    




# @app.route('/status/count', methods = ['GET'])
# def getStatusCount():
#     get_statusdata = tbstatus.query.count()
#     return make_response( jsonify({"status":get_statusdata}) )

# @app.route('/status/<id>', methods = ['GET'])
# def getStatusByID(id):

#     get_statusdata = tbstatus.query.get(id)
#     status_schema = StatusSchema()
#     status_data = status_schema.dump(get_statusdata)
#     return make_response( jsonify({"status":status_data}) )
    
# # delete 
# @app.route('/status/<id>', methods = ['DELETE'])
# def deleteStatusByID(id):

#     get_statusdata = tbstatus.query.get(id)
#     db.session.delete(get_statusdata)
#     db.session.commit()
#     return make_response( jsonify({"status":"deleted status id :" + id}) )

# #update
# @app.route('/status/update', methods = ['PUT'])
# def updateStatusByID(id):
#     data = request.get_json()
    
#     get_statusdata = tbstatus.query.get(int(data['data']['statusid']))
    
#     get_statusdata.statusid = data['data']['statusid']
#     get_statusdata.status = data['data']['status']
#     get_statusdata.details = data['data']['details']
    
#     db.session.add(get_statusdata)
#     db.session.commit()
    
#     status_schema = StatusSchema()
#     status_data = status_schema.dump(get_statusdata)
#     return make_response( jsonify({"status":status_data}) )

# # insert
# @app.route('/status/insert', methods = ['POST'])
# def insertStatusByID():

#     data = request.get_json()
    
#     get_statusdata = tbstatus()
    
#     get_statusdata.statusid = data['data']['statusid']
#     get_statusdata.status = data['data']['status']
#     get_statusdata.details = data['data']['details']
    
#     db.session.add(get_statusdata)
#     db.session.commit()
    
#     status_schema = StatusSchema()
#     status_data = status_schema.dump(get_statusdata)
#     return make_response( jsonify({"status":status_data}) )


app.register_blueprint(bp,url_prefix="/api")
if __name__== '__main__':
    
    app.run()