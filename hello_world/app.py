import awsgi
import json
from flask import (
  Flask,
  Response
)

app = Flask(__name__)

@app.route("/")
def hello():
  dict1 = {"prop1": "p1", "prop2": "p2"}
  return Response(json.dumps(dict1), mimetype='application/json')

@app.route("/test")
def test():
  dict1 = {"prop1": "p1", "prop2": "p2"}
  return Response(json.dumps(dict1), mimetype='application/json')

def lambda_handler(event, context):
  response = awsgi.response(app, event, context)
  response["statusCode"] = int(response["statusCode"])
  return response