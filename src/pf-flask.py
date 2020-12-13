#!/bin/python3


import pythfinder as pf
import json
from flask import Flask, abort, request, Blueprint

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
HEADER = {"Content-Type":"application/json"}

with open("/home/matt/pf-flask/samuel.json") as f:
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
def index():
    message = "Browse to /api/v0/character to view character json"
    status = 404
    out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

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

@bp.route("/character/race", methods = HTTP_METHODS)
def character_race():
    if request.method == "GET":
        data = {
            "race": c.race
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        race = request.json
        keys = race.keys()
        if race and "race" in keys:
            data = race
            c.race = race["race"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'race' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/deity", methods = HTTP_METHODS)
def character_deity():
    if request.method == "GET":
        data = {
            "deity": c.deity
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        deity = request.json
        keys = deity.keys()
        if deity and "deity" in keys:
            data = deity
            c.deity = deity["deity"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'deity' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/homeland", methods = HTTP_METHODS)
def character_homeland():
    if request.method == "GET":
        data = {
            "homeland": c.homeland
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        homeland = request.json
        keys = homeland.keys()
        if homeland and "homeland" in keys:
            data = homeland
            c.homeland = homeland["homeland"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'homeland' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/CMB", methods = HTTP_METHODS)
def character_CMB():
    if request.method == "GET":
        data = {
            "CMB": c.CMB
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        CMB = request.json
        keys = CMB.keys()
        if CMB and "CMB" in keys:
            data = CMB
            c.CMB = CMB["CMB"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'CMB' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/CMD", methods = HTTP_METHODS)
def character_CMD():
    if request.method == "GET":
        data = {
            "CMD": c.CMD
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        CMD = request.json
        keys = CMD.keys()
        if CMD and "CMD" in keys:
            data = CMD
            c.CMD = CMD["CMD"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'CMD' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/initiativeMods", methods = HTTP_METHODS)
def character_initiativeMods():
    if request.method == "GET":
        data = {
            "initiativeMods": c.initiativeMods
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        initiativeMods = request.json
        keys = initiativeMods.keys()
        if initiativeMods and "initiativeMods" in keys:
            data = initiativeMods
            c.initiativeMods = initiativeMods["initiativeMods"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'initiativeMods' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/alignment", methods = HTTP_METHODS)
def character_alignment():
    if request.method == "GET":
        data = {
            "alignment": c.alignment
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        alignment = request.json
        keys = alignment.keys()
        if alignment and "alignment" in keys:
            data = alignment
            c.alignment = alignment["alignment"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'alignment' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/description", methods = HTTP_METHODS)
def character_description():
    if request.method == "GET":
        data = {
            "description": c.description
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        description = request.json
        keys = description.keys()
        if description and "description" in keys:
            data = description
            c.description = description["description"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'description' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/height", methods = HTTP_METHODS)
def character_height():
    if request.method == "GET":
        data = {
            "height": c.height
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        height = request.json
        keys = height.keys()
        if height and "height" in keys:
            data = height
            c.height = height["height"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'height' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/weight", methods = HTTP_METHODS)
def character_weight():
    if request.method == "GET":
        data = {
            "weight": c.weight
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        weight = request.json
        keys = weight.keys()
        if weight and "weight" in keys:
            data = weight
            c.weight = weight["weight"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'weight' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/size", methods = HTTP_METHODS)
def character_size():
    if request.method == "GET":
        data = {
            "size": c.size
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        size = request.json
        keys = size.keys()
        if size and "size" in keys:
            data = size
            c.size = size["size"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'size' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/age", methods = HTTP_METHODS)
def character_age():
    if request.method == "GET":
        data = {
            "age": c.age
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        age = request.json
        keys = age.keys()
        if age and "age" in keys:
            data = age
            c.age = age["age"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'age' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/hair", methods = HTTP_METHODS)
def character_hair():
    if request.method == "GET":
        data = {
            "hair": c.hair
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        hair = request.json
        keys = hair.keys()
        if hair and "hair" in keys:
            data = hair
            c.hair = hair["hair"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'hair' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/eyes", methods = HTTP_METHODS)
def character_eyes():
    if request.method == "GET":
        data = {
            "eyes": c.eyes
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        eyes = request.json
        keys = eyes.keys()
        if eyes and "eyes" in keys:
            data = eyes
            c.eyes = eyes["eyes"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'eyes' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/languages", methods = HTTP_METHODS)
def character_languages():
    if request.method == "GET":
        data = {
            "languages": c.languages
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        languages = request.json
        keys = languages.keys()
        if languages and "languages" in keys:
            data = languages
            c.languages = languages["languages"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'languages' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/spellsPerDay", methods = HTTP_METHODS)
def character_spellsPerDay():
    if request.method == "GET":
        data = {
            "spellsPerDay": c.spellsPerDay
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        spellsPerDay = request.json
        keys = spellsPerDay.keys()
        if spellsPerDay and "spellsPerDay" in keys:
            data = spellsPerDay
            c.spellsPerDay = spellsPerDay["spellsPerDay"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'spellsPerDay' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/baseAttackBonus", methods = HTTP_METHODS)
def character_baseAttackBonus():
    if request.method == "GET":
        data = {
            "baseAttackBonus": c.baseAttackBonus
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        baseAttackBonus = request.json
        keys = baseAttackBonus.keys()
        if baseAttackBonus and "baseAttackBonus" in keys:
            data = baseAttackBonus
            c.baseAttackBonus = baseAttackBonus["baseAttackBonus"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'baseAttackBonus' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/gold", methods = HTTP_METHODS)
def character_gold():
    if request.method == "GET":
        data = {
            "gold": c.gold
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        gold = request.json
        keys = gold.keys()
        if gold and "gold" in keys:
            data = gold
            c.gold = gold["gold"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'gold' key."
            status = 400
            out = return_json(message = message, status = status)
    else:
        out = return_bad_request()
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/AC", methods = HTTP_METHODS)
def character_AC():
    if request.method == "GET":
        data = {
            "AC": c.AC
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        AC = request.json
        keys = AC.keys()
        if AC and "AC" in keys:
            data = AC
            c.AC = AC["AC"]
            out = return_json(data = data)
        else:
            message = "Improper data format: JSON must contain a 'AC' key."
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
