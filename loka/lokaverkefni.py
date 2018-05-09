#Fannar Hrafn Haraldsson
#lokaverkefni vor 2018
from bottle import template,route,run,static_file
import json
with open("json/gogn.json","r") as skra:
    gogn = json.load(skra)
skra.close()
print(gogn['data'][0]['img'])
for i in gogn['data']:
    print(i['img'])
@route('/')
def index():
        return template('index.tpl',gogn=gogn)
#bendi á static skráina og að allt í henni sé static
@route('/maze')
def maze():
    return
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

run()