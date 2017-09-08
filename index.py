from bottle import route, run, template
import random

@route('/')
def index():
    return template('views/index.tpl')

run(host='localhost', port=8000)