#!/bin/python3


import pythfinder as pf
import json
from flask import Flask, abort, request

with open("/home/matt/pythfinder-flask/samuel.json") as f:
    c = pf.Character(json.load(f))

app = Flask(__name__)

@app.route("/")
def hey():
    return "Browse to /character to view character json"

@app.route("/character")
def character():
    return c.getJson()

@app.route("/character/name")
def character_name():
    return c.name

@app.route("/character/equipment")
def character_equipment():
    #filter_data = dict(request.args) if request.args else {}
    #return json.dumps(c.get_item(data = filter_data))
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
    return json.dumps(c.get_item(name = name,
                                 weight = weight,
                                 count = count,
                                 camp = camp,
                                 on_person = on_person,
                                 location = location,
                                 notes = notes))
