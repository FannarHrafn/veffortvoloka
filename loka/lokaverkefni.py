#Fannar Hrafn Haraldsson
#lokaverkefni vor 2018
from bottle import template,route,run,static_file
import json
with open("json/gogn.json","r") as skra:
    gogn = json.load(skra)
skra.close()
innerhtml="<div>\n"
for i in gogn['data']:
    print(i['tags'])
    line = "<a data-tags='"+i['tags']+"' href="+i['link']+" > <img src='/static/"+i['img']+"' alt='"+i['nafn']+"'></a>\n"
    innerhtml += line
innerhtml += "</div>"
print(innerhtml)
@route('/')
def index():
        return template('views/index.tpl',lines=innerhtml)
@route('/defence/shielder.html')
def shielder():
    return template('defence/shielder.html')
@route('/maze/www/maze.html')
def maze():
    return template('maze/www/maze.html')
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')
run()
