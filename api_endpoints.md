# API endpoints
This document describes the API endpoint structure for the Flask 
implementation of the pythfinder module.

## A note on names
The pythfinder module enforces unique names for collection properties, 
like equipment, attacks, spells, etc. This is to ensure that things 
like update\_feat only affect a single resource, and that the selection 
is not ambiguous or arbitrary. Now, I _could_ use UUIDs, but I figured 
unique names would be easier to reason about and implement, for both 
myself and users.

## A note on collections
Many properties in the Character class are represented as lists, 
containing multiple different entries of dictionaries. Examples include 
equipment, attacks, spells, etc. With these properties, the results 
of a GET request will always be returned as a list, even if the request 
only returns one result. This simplifies the implementation on both 
ends, as you can always assume the result is iterable.

## Attributes/Methods ->Endpoints
```
import pythfinder as pf
c = pf.Character()
```

Each simple property will map directly to a url:

c.name            -> /character/name
c.race            -> /character/race
c.deity           -> /character/deity
c.homeland        -> /character/homeland
c.CMB             -> /character/CMB
c.CMD             -> /character/CMD
c.initiativeMods  -> /character/initiativeMods
c.alignment       -> /character/alignment
c.description     -> /character/description
c.height          -> /character/height
c.weight          -> /character/weight
c.size            -> /character/size
c.age             -> /character/age
c.hair            -> /character/hair
c.eyes            -> /character/eyes
c.languages       -> /character/languages
c.spellsPerDay    -> /character/spellsPerDay
c.baseAttackBonus -> /character/baseAttackBonus
c.gold            -> /character/gold
c.AC              -> /character/AC

GET requests will return the element, while PUT requests will update 
the element with the new value.

Examples:

```
PUT /character/homeland
body:
{
    "homeland": "Funkytown"
}

PUT /character/AC
body:
{
    "AC": [5, -2, 1]
}
```

Complex properties will map to their add, update, and delete methods, 
depending on the request, the URI, and the body.

For example, classes:
c.get_class()                                      -> GET /character/classes
c.update_class(name = class name)                  -> PATCH /character/classes/class name
c.delete_element(name = class name, type_ = class) -> DELETE /character/classes/class name

```
GET /character/classes?name=Fighter&level={"lt": 4}
```
