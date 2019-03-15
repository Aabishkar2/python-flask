from flask import Flask
from flask import jsonify 
from flask import request
from flask import render_template
from flask_cors import CORS
import json
from controllers.NepseController import nepseJSON

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return nepseJSON()

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')