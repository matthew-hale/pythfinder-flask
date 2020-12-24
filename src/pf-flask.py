#!/bin/python3

import pythfinder as pf
import json
from flask import Flask, abort, request, Blueprint, session, g
from uuid import uuid4 as uuid
from redis import Redis
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

TIMEOUT = 14*24*60*60 # timeout in seconds; == 14 days
HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
HEADER = {
    "Content-Type": "application/json",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "http://localhost:8000",
    "Access-Control-Allow-Methods": "*"
}

# initialize redis connector
r = Redis(host = "localhost", port = 6379, db = 0, decode_responses = True)

bp = Blueprint('pythfinder-flask', __name__, url_prefix = "/api/v0")
CORS(bp, supports_credentials = True)
app = Flask(__name__)

# secret development key (set this locally in config for deployment)
app.secret_key = b"this is the development server key for testing, please don't use this in production!"

def return_json(status = 200, message = "", data = {}):
    return {
        "status": status,
        "message": message,
        "data": data
    }

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps(return_json(status = e.code, message = str(e)))
    response.headers = HEADER
    return response

@app.before_request
def setup_request_context():
    session_keys = session.keys()
    # Fresh session; generate new id
    if "id" not in session_keys:
        session["id"] = str(uuid())
    if not r.exists(session["id"]):
        blank_character = pf.Character()
        raw_json = blank_character.get_json()
        r.set(session["id"], raw_json)
    c_data = json.loads(r.get(session["id"]))
    g.c = pf.Character(data = c_data)

@app.after_request
def cache_character(response):
    c_data = g.c.get_json()
    r.set(session["id"], c_data)
    r.expire(session["id"], TIMEOUT)
    return response

@app.route("/")
def index():
    abort(404, description = "browse to /api/v0/character to view character json")

@bp.route("/character", methods = ["GET", "PUT"])
def character():
    if request.method == "GET":
        data = json.loads(g.c.get_json())
        out = return_json(data = data)
    elif request.method == "PUT":
        new_c = request.get_json()
        if new_c:
            new_c_character = pf.Character(data = new_c)
            new_c_json = new_c_character.get_json()
            r.set(session["id"], new_c_json)
            g.c = pf.Character(data = json.loads(r.get(session["id"])))
            return "", 204, HEADER
        else:
            abort(400, description = "invalid character data or content type")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/name", methods = ["GET", "PUT"])
def character_name():
    if request.method == "GET":
        data = {
            "name": g.c.name
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        name = request.get_json()
        keys = name.keys()
        if name and "name" in keys:
            data = name
            g.c.name = name["name"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'name' key")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/race", methods = ["GET", "PUT"])
def character_race():
    if request.method == "GET":
        data = {
            "race": g.c.race
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        race = request.get_json()
        keys = race.keys()
        if race and "race" in keys:
            data = race
            g.c.race = race["race"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'race' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/deity", methods = ["GET", "PUT"])
def character_deity():
    if request.method == "GET":
        data = {
            "deity": g.c.deity
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        deity = request.get_json()
        keys = deity.keys()
        if deity and "deity" in keys:
            data = deity
            g.c.deity = deity["deity"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'deity' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/homeland", methods = ["GET", "PUT"])
def character_homeland():
    if request.method == "GET":
        data = {
            "homeland": g.c.homeland
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        homeland = request.get_json()
        keys = homeland.keys()
        if homeland and "homeland" in keys:
            data = homeland
            g.c.homeland = homeland["homeland"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'homeland' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/CMB", methods = ["GET", "PUT"])
def character_CMB():
    if request.method == "GET":
        data = {
            "CMB": g.c.CMB
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        CMB = request.get_json()
        keys = CMB.keys()
        if CMB and "CMB" in keys:
            data = CMB
            g.c.CMB = CMB["CMB"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'CMB' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/CMD", methods = ["GET", "PUT"])
def character_CMD():
    if request.method == "GET":
        data = {
            "CMD": g.c.CMD
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        CMD = request.get_json()
        keys = CMD.keys()
        if CMD and "CMD" in keys:
            data = CMD
            g.c.CMD = CMD["CMD"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'CMD' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/initiative_mods", methods = ["GET", "PUT"])
def character_initiative_mods():
    if request.method == "GET":
        data = {
            "initiative_mods": g.c.initiative_mods
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        initiative_mods = request.get_json()
        keys = initiative_mods.keys()
        if initiative_mods and "initiative_mods" in keys:
            data = initiative_mods
            g.c.initiative_mods = initiative_mods["initiative_mods"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'initiative_mods' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/alignment", methods = ["GET", "PUT"])
def character_alignment():
    if request.method == "GET":
        data = {
            "alignment": g.c.alignment
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        alignment = request.get_json()
        keys = alignment.keys()
        if alignment and "alignment" in keys:
            data = alignment
            g.c.alignment = alignment["alignment"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'alignment' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/description", methods = ["GET", "PUT"])
def character_description():
    if request.method == "GET":
        data = {
            "description": g.c.description
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        description = request.get_json()
        keys = description.keys()
        if description and "description" in keys:
            data = description
            g.c.description = description["description"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'description' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/height", methods = ["GET", "PUT"])
def character_height():
    if request.method == "GET":
        data = {
            "height": g.c.height
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        height = request.get_json()
        keys = height.keys()
        if height and "height" in keys:
            data = height
            g.c.height = height["height"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'height' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/weight", methods = ["GET", "PUT"])
def character_weight():
    if request.method == "GET":
        data = {
            "weight": g.c.weight
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        weight = request.get_json()
        keys = weight.keys()
        if weight and "weight" in keys:
            data = weight
            g.c.weight = weight["weight"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'weight' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/size", methods = ["GET", "PUT"])
def character_size():
    if request.method == "GET":
        data = {
            "size": g.c.size
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        size = request.get_json()
        keys = size.keys()
        if size and "size" in keys:
            data = size
            g.c.size = size["size"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'size' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/age", methods = ["GET", "PUT"])
def character_age():
    if request.method == "GET":
        data = {
            "age": g.c.age
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        age = request.get_json()
        keys = age.keys()
        if age and "age" in keys:
            data = age
            g.c.age = age["age"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'age' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/hair", methods = ["GET", "PUT"])
def character_hair():
    if request.method == "GET":
        data = {
            "hair": g.c.hair
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        hair = request.get_json()
        keys = hair.keys()
        if hair and "hair" in keys:
            data = hair
            g.c.hair = hair["hair"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'hair' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/eyes", methods = ["GET", "PUT"])
def character_eyes():
    if request.method == "GET":
        data = {
            "eyes": g.c.eyes
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        eyes = request.get_json()
        keys = eyes.keys()
        if eyes and "eyes" in keys:
            data = eyes
            g.c.eyes = eyes["eyes"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'eyes' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/languages", methods = ["GET", "PUT"])
def character_languages():
    if request.method == "GET":
        data = {
            "languages": g.c.languages
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        languages = request.get_json()
        keys = languages.keys()
        if languages and "languages" in keys:
            data = languages
            g.c.languages = languages["languages"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'languages' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/spells_per_day", methods = ["GET", "PUT"])
def character_spells_per_day():
    if request.method == "GET":
        data = {
            "spells_per_day": g.c.spells_per_day
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        spells_per_day = request.get_json()
        keys = spells_per_day.keys()
        if spells_per_day and "spells_per_day" in keys:
            data = spells_per_day
            g.c.spells_per_day = spells_per_day["spells_per_day"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'spells_per_day' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/base_attack_bonus", methods = ["GET", "PUT"])
def character_base_attack_bonus():
    if request.method == "GET":
        data = {
            "base_attack_bonus": g.c.base_attack_bonus
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        base_attack_bonus = request.get_json()
        keys = base_attack_bonus.keys()
        if base_attack_bonus and "base_attack_bonus" in keys:
            data = base_attack_bonus
            g.c.base_attack_bonus = base_attack_bonus["base_attack_bonus"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'base_attack_bonus' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/gold", methods = ["GET", "PUT"])
def character_gold():
    if request.method == "GET":
        data = {
            "gold": g.c.gold
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        gold = request.get_json()
        keys = gold.keys()
        if gold and "gold" in keys:
            data = gold
            g.c.gold = gold["gold"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'gold' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/AC", methods = ["GET", "PUT"])
def character_AC():
    if request.method == "GET":
        data = {
            "AC": g.c.AC
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        AC = request.get_json()
        keys = AC.keys()
        if AC and "AC" in keys:
            data = AC
            g.c.AC = AC["AC"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'AC' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/speed", methods = ["GET", "PUT"])
def character_speed():
    if request.method == "GET":
        data = {
            "speed": g.c.speed
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        speed = request.get_json()
        keys = speed.keys()
        if speed and "speed" in keys:
            data = speed
            g.c.speed = speed["speed"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'speed' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/hp", methods = ["GET", "PUT"])
def character_hp():
    if request.method == "GET":
        data = {
            "hp": g.c.hp
        }
        out = return_json(data = data)
    elif request.method == "PUT":
        hp = request.get_json()
        keys = hp.keys()
        if hp and "hp" in keys:
            data = hp
            g.c.hp = hp["hp"]
            out = return_json(data = data)
        else:
            abort(400, description = "improper data format: JSON must contain a 'hp' key.")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/equipment", methods = ["GET", "POST"])
def character_equipment():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        uuid = request.args.get("uuid") if request.args.get("uuid") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        weight = request.args.get("weight") if request.args.get("weight") else {}
        if weight:
            weight = json.loads(str(request.args.get("weight")).replace("'", '"')) 
        count = request.args.get("count") if request.args.get("count") else {}
        if count:
            count = json.loads(str(request.args.get("count")).replace("'", '"')) 
        camp = request.args.get("camp").split(",") if request.args.get("camp") else []
        on_person = request.args.get("on_person").split(",") if request.args.get("on_person") else []
        location = request.args.get("location").split(",") if request.args.get("location") else []
        notes = request.args.get("notes").split(",") if request.args.get("notes") else []
        get_data = {
            "name": name,
            "uuid": uuid,
            "name_search_type": name_search_type,
            "weight": weight,
            "count": count,
            "camp": camp,
            "on_person": on_person,
            "location": location,
            "notes": notes
        }
        try:
            data = g.c.get_equipment(data = get_data)
            out_list = [d.__dict__ for d in data]
            out = return_json(data = out_list)
        except (KeyError, ValueError) as err:
            abort(400, description = "pythfinder error: {}".format(err))
    elif request.method == "POST":
        post_data = request.get_json()
        if post_data:
            try:
                item = g.c.add_equipment(data = post_data)
                out = return_json(data = item.__dict__, status = 201)
            except ValueError as err:
                abort(400, description = "pythfinder error: {}".format(err))
        else:
            abort(400, description = "invalid post data")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/equipment/<uuid>", methods = ["GET", "PATCH", "DELETE"])
def character_equipment_specific(uuid):
    item_list = g.c.get_equipment(uuid = uuid)
    if not item_list:
        abort(404, description = "item not found with uuid '{}'".format(uuid))
    item = item_list[0]
    if request.method == "GET":
        out = return_json(data = item.__dict__)
    elif request.method == "PATCH":
        patch_data = request.get_json()
        if patch_data:
            try:
                data = item.update(data = patch_data)
                out = return_json(data = data.__dict__)
            except ValueError as err:
                abort(400, description = "pythfinder error: {}".format(err))
        else:
            abort(400, description = "invalid patch data")
    elif request.method == "DELETE":
        try:
            g.c.delete_item(uuid = uuid)
        except ValueError as err:
            abort(400, description = "pythfinder error: {}".format(err))
        else:
            return "", 204, HEADER
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/abilities", methods = ["GET"])
def character_abilities():
    name = request.args.get("name").split(",") if request.args.get("name") else []
    name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
    base = request.args.get("base") if request.args.get("base") else {}
    if base:
        base = json.loads(str(request.args.get("base")).replace("'", '"')) 
    misc = request.args.get("misc") if request.args.get("misc") else {}
    if misc:
        misc = json.loads(str(request.args.get("misc")).replace("'", '"')) 
    get_data = {
        "name": name,
        "name_search_type": name_search_type,
        "base": base,
        "misc": misc
    }
    try:
        data = g.c.get_ability(data = get_data)
        out = return_json(data = data)
    except (KeyError, ValueError) as err:
        abort(400, description = "pythfinder error: {}".format(err))
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/abilities/<name>", methods = ["GET", "PATCH"])
def character_abilities_specific(name):
    ability = g.c.get_ability(name = name, name_search_type = "absolute") 
    if not ability:
        abort(404, description = "ability not found with name '{}'".format(name))
    if request.method == "GET":
        out = return_json(data = ability)
    elif request.method == "PATCH":
        patch_data = request.get_json()
        if patch_data:
            try:
                data = g.c.update_ability(name = name, data = patch_data)
                out = return_json(data = data)
            except ValueError as err:
                abort(400, description = "pythfinder error: {}".format(err))
        else:
            abort(400, description = "invalid patch data")
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/saving_throws", methods = HTTP_METHODS)
def character_saving_throws():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        base = request.args.get("base") if request.args.get("base") else {}
        if base:
            base = json.loads(str(request.args.get("base")).replace("'", '"')) 
        misc = request.args.get("misc") if request.args.get("misc") else {}
        if misc:
            misc = json.loads(str(request.args.get("misc")).replace("'", '"')) 
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "base": base,
            "misc": misc
        }
        try:
            data = g.c.get_saving_throw(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/classes", methods = HTTP_METHODS)
def character_classes():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        archetypes = request.args.get("archetypes").split(",") if request.args.get("archetypes") else []
        level = request.args.get("level") if request.args.get("level") else {}
        if level:
            level = json.loads(str(request.args.get("level")).replace("'", '"')) 
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "archetypes": archetypes,
            "level": level
        }
        try:
            data = g.c.get_class(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/feats", methods = HTTP_METHODS)
def character_feats():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        description = request.args.get("description").split(",") if request.args.get("description") else []
        notes = request.args.get("notes").split(",") if request.args.get("notes") else []
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "description": description,
            "notes": notes
        }
        try:
            data = g.c.get_feat(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/traits", methods = HTTP_METHODS)
def character_traits():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        description = request.args.get("description").split(",") if request.args.get("description") else []
        notes = request.args.get("notes").split(",") if request.args.get("notes") else []
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "description": description,
            "notes": notes
        }
        try:
            data = g.c.get_trait(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/special", methods = HTTP_METHODS)
def character_special():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        description = request.args.get("description").split(",") if request.args.get("description") else []
        notes = request.args.get("notes").split(",") if request.args.get("notes") else []
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "description": description,
            "notes": notes
        }
        try:
            data = g.c.get_special(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/skills", methods = HTTP_METHODS)
def character_skills():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        rank = request.args.get("rank") if request.args.get("rank") else {}
        if rank:
            rank = json.loads(str(request.args.get("rank")).replace("'", '"')) 
        if request.args.get("isClass") == None:
            isClass = []
        else:
            isClass = request.args.get("isClass") == "true"
        mod = request.args.get("mod").split(",") if request.args.get("mod") else []
        notes = request.args.get("notes").split(",") if request.args.get("notes") else []
        if request.args.get("useUntrained") == None:
            useUntrained = []
        else:
            useUntrained = request.args.get("useUntrained") == "true"
        misc = request.args.get("misc") if request.args.get("misc") else {}
        if misc:
            misc = json.loads(str(request.args.get("misc")).replace("'", '"')) 
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "rank": rank,
            "isClass": isClass,
            "mod": mod,
            "notes": notes,
            "useUntrained": useUntrained,
            "misc": misc
        }
        try:
            data = g.c.get_skill(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/spells", methods = HTTP_METHODS)
def character_spells():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        level = request.args.get("level") if request.args.get("level") else {}
        if level:
            level = json.loads(str(request.args.get("level")).replace("'", '"')) 
        description = request.args.get("description").split(",") if request.args.get("description") else []
        prepared = request.args.get("prepared") if request.args.get("prepared") else {}
        if prepared:
            prepared = json.loads(str(request.args.get("prepared")).replace("'", '"')) 
        cast = request.args.get("cast") if request.args.get("cast") else {}
        if cast:
            cast = json.loads(str(request.args.get("cast")).replace("'", '"')) 
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "level": level,
            "description": description,
            "prepared": prepared,
            "cast": cast
        }
        try:
            data = g.c.get_spell(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/armor", methods = HTTP_METHODS)
def character_armor():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        acBonus = request.args.get("acBonus") if request.args.get("acBonus") else {}
        if acBonus:
            acBonus = json.loads(str(request.args.get("acBonus")).replace("'", '"')) 
        acPenalty = request.args.get("acPenalty") if request.args.get("acPenalty") else {}
        if acPenalty:
            acPenalty = json.loads(str(request.args.get("acPenalty")).replace("'", '"')) 
        maxDexBonus = request.args.get("maxDexBonus") if request.args.get("maxDexBonus") else {}
        if maxDexBonus:
            maxDexBonus = json.loads(str(request.args.get("maxDexBonus")).replace("'", '"')) 
        arcaneFailureChance = request.args.get("arcaneFailureChance") if request.args.get("arcaneFailureChance") else {}
        if arcaneFailureChance:
            arcaneFailureChance = json.loads(str(request.args.get("arcaneFailureChance")).replace("'", '"')) 
        type_ = request.args.get("type").split(",") if request.args.get("type") else []
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "acBonus": acBonus,
            "acPenalty": acPenalty,
            "maxDexBonus": maxDexBonus,
            "arcaneFailureChance": arcaneFailureChance,
            "type": type_,
        }
        try:
            data = g.c.get_armor(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

@bp.route("/character/attacks", methods = HTTP_METHODS)
def character_attacks():
    if request.method == "GET":
        name = request.args.get("name").split(",") if request.args.get("name") else []
        name_search_type = request.args.get("name_search_type") if request.args.get("name_search_type") else ""
        attackType = request.args.get("attackType").split(",") if request.args.get("attackType") else []
        damageType = request.args.get("damageType").split(",") if request.args.get("damageType") else []
        attack_mod = request.args.get("attack_mod").split(",") if request.args.get("attack_mod") else []
        damage_mod = request.args.get("damage_mod").split(",") if request.args.get("damage_mod") else []
        damage = request.args.get("damage").split(",") if request.args.get("damage") else []
        critRoll = request.args.get("critRoll") if request.args.get("critRoll") else {}
        if critRoll:
            critRoll = json.loads(str(request.args.get("critRoll")).replace("'", '"')) 
        critMulti = request.args.get("critMulti") if request.args.get("critMulti") else {}
        if critMulti:
            critMulti = json.loads(str(request.args.get("critMulti")).replace("'", '"')) 
        range_ = request.args.get("range") if request.args.get("range") else {}
        if range_:
            range_ = json.loads(str(request.args.get("range")).replace("'", '"')) 
        notes = request.args.get("notes").split(",") if request.args.get("notes") else []
        get_data = {
            "name": name,
            "name_search_type": name_search_type,
            "attackType": attackType,
            "damageType": damageType,
            "attack_mod": attack_mod,
            "damage_mod": damage_mod,
            "damage": damage,
            "critRoll": critRoll,
            "critMulti": critMulti,
            "range": range_,
            "notes": notes
        }
        try:
            data = g.c.get_attack(data = get_data)
            out = return_json(data = data)
        except (KeyError, ValueError) as err:
            message = "pythfinder error: {}".format(err)
            status = 400
            out = return_json(message = message, status = status)
    return json.dumps(out), out["status"], HEADER

app.register_blueprint(bp)
