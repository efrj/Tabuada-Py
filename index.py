from bottle import route, run, template
import random

@route('/')
def index():
    return template ('views/index.tpl', colors=['#cb3d00', '#336699', '#521515', '#478244', '#8f2525', '#4e5b6e', '#ff5a36', '#004b26', '#295398', '#6f0000'])

run(host='localhost', port=8000)