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
    return json.dumps(c.name)

@app.route("/character/race")
def character_race():
    return json.dumps(c.race)

@app.route("/character/deity")
def character_deity():
    return json.dumps(c.deity)

@app.route("/character/homeland")
def character_homeland():
    return json.dumps(c.homeland)

@app.route("/character/CMB")
def character_CMB():
    return json.dumps(c.CMB)

@app.route("/character/CMD")
def character_CMD():
    return json.dumps(c.CMD)

@app.route("/character/alignment")
def character_alignment():
    return json.dumps(c.alignment)

@app.route("/character/description")
def character_description():
    return json.dumps(c.description)

@app.route("/character/height")
def character_height():
    return json.dumps(c.height)

@app.route("/character/weight")
def character_weight():
    return json.dumps(c.weight)

@app.route("/character/size")
def character_size():
    return json.dumps(c.size)

@app.route("/character/age")
def character_age():
    return json.dumps(c.age)

@app.route("/character/hair")
def character_hair():
    return json.dumps(c.hair)

@app.route("/character/eyes")
def character_eyes():
    return json.dumps(c.eyes)

@app.route("/character/baseAttackBonus")
def character_baseAttackBonus():
    return json.dumps(c.baseAttackBonus)

@app.route("/character/gold")
def character_gold():
    return json.dumps(c.gold)

@app.route("/character/initiativeMods")
def character_initiativeMods():
    return json.dumps(c.initiativeMods)

@app.route("/character/AC")
def character_AC():
    return json.dumps(c.AC)

@app.route("/character/spellsPerDay")
def character_spellsPerDay():
    return json.dumps(c.spellsPerDay)

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
