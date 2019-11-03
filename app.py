#
# Author Information
#
_author__ = 'Akhil Bidhuri <akhilbidhuri@gmail.com>'
__copyright__ = 'Nothing But you can do better'
__maintainer__ = 'Akhil Bidhuri'
__email__ = 'akhilbidhuri@gmail.com'
__date__ = 'Nov 1, 2019'
__version__ = 1.0


#
# Imports
#
import os, jwt, datetime
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker

#
# Setting up App
#
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
cors = CORS(app, resources=r'/*')

db = SQLAlchemy(app)

#
# Decorator for Validating tokens
#


from db_utils import *
def token_required(f):
    '''
        Decorator for validating the token. 
    '''
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('token', 0)
        if token==0:
            return jsonify({'msg':'Token Missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'msg':'Invalid Token Request For new Token'})
        return f(*args, **kwargs)
    return decorated


#
# Routes
#
@app.route('/', methods=['POST', 'GET'])
@cross_origin(origin='*')
def mainroute():
    return "WELCOME TO THE BANK4U Service, Head to https://github.com/akhilbidhuri/bank4u for details of endpoints and more!!!"

@app.route('/api/v1/getToken', methods=['POST', 'GET'])
@cross_origin(origin='*')
def getToken():
    '''
        Desceription : Endpoint to get the token WHICH is valid for only 5 days.
        Accepts POST/GET request.
        Params : Expects Nothing.
        Returns : a JWT in JSON.
    '''
    token = jwt.encode({'exp': datetime.datetime.now() + datetime.timedelta(days=5)}, app.config['SECRET_KEY'])
    return jsonify({'token':token.decode('utf-8')})

@app.route('/api/v1/getDetails', methods=['GET'])
@cross_origin(origin='*')
@token_required
def getDetails():
    '''
        Desceription : Endpoint to get the bank details given the IFSC.
        Accepts GET request.
        Params : Expects JWT in header and IFSC in param.
        Returns : bank details if IFSC exists in Database otherwise an error message in JSON Format.
    '''
    try:
        ifsc = request.args['ifsc']
    except:
        return jsonify({'msg': 'IFSC not provided.'}), 400
    return getDet(ifsc)

@app.route('/api/v1/getBranches', methods=['GET'])
@cross_origin(origin='*')
@token_required
def getBranches():
    '''
        Desceription : Endpoint to fetch all details of branches, given bank name and a city. This API should also support limit and offset parameters.
        Accepts GET request.
        Params : Expects JWT in header and bank name, city, offset(optional), limit(optional) in params.
        Returns : branches details if bank name & city exists in Database otherwise an error message in JSON Format.
        Default values: offset=1, limit=10
    '''
    default_offset, default_limit = 1, 10
    try:
        bank_name = request.args['bank_name'].replace('+', ' ')
        city = request.args['city'].replace('+', ' ')
        offset = int(request.args.get('offset', default_offset))
        limit = int(request.args.get('limit', default_limit))
    except:
        return jsonify({'msg': 'Wrong Params provided.'}), 400
    return getBranch(bank_name, city, offset, limit)

#
# Main runs the Flask App on port 6543(no specific reason behind choosing it)
#
if __name__ == "__main__":
    app.run(port=6543, debug=True)