#Fannar Hrafn Haraldsson
#lokaverkefni vor 2018
from bottle import template,route,run,static_file
#næ í gögn frá json skrá
import json
with open("json/gogn.json","r") as skra:
    gogn = json.load(skra)
skra.close()
#byggi html í python skránni til að komast framhjá vandamálum  við embedded  python kóða í template
innerhtml="<div>\n"
for i in gogn['data']:
    print(i['tags'])
    line = "<a data-tags='"+i['tags']+"' href="+i['link']+" > <img src='/static/"+i['img']+"' alt='"+i['nafn']+"'></a>\n"
    innerhtml += line
innerhtml += "</div>"
print(innerhtml)
#routes fyrir index, fyrsta leikinn og seinni leikinn
@route('/')
def index():
        return template('views/index.tpl',lines=innerhtml)
@route('/defence/shielder.html')
def shielder():
    return template('defence/shielder.html')
#seinni leikurinn virkar samt ekki á síðunni þar sem  RPG Maker vinnur víst ekki vel með bottle
#þar sem það þarf að vera frjálst til að ná í hvaða gögn  sem það vill
#en leikurinn virkar fínt fyrir utan bottle  svo ég veit að þetta  er bottle tengt
@route('/maze/www/maze.html')
def maze():
    return template('maze/www/maze.html')
#static files  fyrir index  síðuna og defence, hef reynt  að gera það sama fyrir öll js files á  seinni leiknum
#en þar sem  hann nær ekki í öll gögnin sín í einu þá lenti ég líka í vandamálum þar
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')
@route('/defence/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./defence/js')
run()
