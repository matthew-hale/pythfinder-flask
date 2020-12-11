#!/bin/python3


import pythfinder as pf
import json
from flask import Flask, abort, request, Blueprint

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
HEADER = {"Content-Type":"application/json"}

with open("/home/matt/pythfinder-flask/samuel.json") as f:
    c = pf.Character(json.load(f))

bp = Blueprint('pythfinder-flask', __name__, url_prefix = "/api/v0")
app = Flask(__name__)

def return_json(status = 200, message = "", data = {}):
    return {
        "status": status,
        "message": message,
        "data": data
    }

def return_bad_request():
    return return_json(status = 405, message = "Bad request type")

@app.route("/")
def hey():
    return "Browse to /api/v0/character to view character json"

@bp.route("/character")
def character():
    data = json.loads(c.getJson())
    out = return_json(data = data)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/name", methods = HTTP_METHODS)
def character_name():
    if request.method == "GET":
        data = {
            "name": c.name
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        name = request.json
        keys = name.keys()
        if name and "name" in keys:
            data = name
            c.name = name["name"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'name' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/equipment", methods = HTTP_METHODS)
def character_equipment():
    if request.method == "GET":
        name = request.args.get("name") if request.args.get("name") else []
        weight = request.args.get("weight") if request.args.get("weight") else {}
        if weight:
            weight = json.loads(str(request.args.get("weight")).replace("'", '"')) 
        count = request.args.get("count") if request.args.get("count") else {}
        if count:
            count = json.loads(str(request.args.get("count")).replace("'", '"')) 
        camp = request.args.get("camp") if request.args.get("camp") else []
        on_person = request.args.get("on_person") if request.args.get("on_person") else []
        location = request.args.get("location") if request.args.get("location") else []
        notes = request.args.get("notes") if request.args.get("notes") else []
        get_data = {
            "name": name,
            "weight": weight,
            "count": count,
            "camp": camp,
            "on_person": on_person,
            "location": location,
            "notes": notes
        }
        try:
            data = c.get_item(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

app.register_blueprint(bp)
