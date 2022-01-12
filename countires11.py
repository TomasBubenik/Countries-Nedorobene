import json
from json.encoder import HAS_UTF8
from os import getpid, name
with open("countries.json",encoding="utf-8") as f:
    data = json.load(f)

Populacia = {}
Velkost = {}
Hustota = {}
Gdpa = {}
Kontinenty = {}
Katastory = {}
for i in data:
    a=i["Population"].split()
    Populacia[i["Name"]]=int(a[0])

    b=(i["Area"]).split()
    Velkost[i["Name"]]=max(1,int(b[0]))
    
    Gdpa[i["Name"]]=i["GDP"]

    Hustota[i["Name"]]=Populacia[i["Name"]]/Velkost[i["Name"]]
    
    Katastory[i["Continent"]]=i["NaturalHazards"]

