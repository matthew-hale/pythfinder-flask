#!/bin/python3


import pythfinder as pf
import json
from flask import Flask, abort, request

with open("/home/matt/pythfinder/test.json") as f:
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
    if request.args:
        return json.dumps(pf.filter_list(c.equipment, request.args))
    else:
        return json.dumps(c.equipment)

@app.route("/character/equipment/name:<name>")
def character_equipment_name(name):
    out = None
    for item in c.equipment:
        if item["name"] == name:
            out = json.dumps(item)
    if not out:
        abort(404)
    else:
        return out
