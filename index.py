from bottle import run, route, template, static_file
import random
import pdfkit

@route('/')
def index():
	colors=['#cb3d00','#336699','#521515','#478244','#8f2525','#4e5b6e','#ff5a36','#004b26','#295398','#6f0000']
	return template('views/index.tpl',colors=colors)

@route('/pdf')
def pdf():
	pdfkit.from_url('http://localhost:8080', 'tabuada.pdf')

@route('/assets/css/<filename>')
def server_static(filename):
	return static_file(filename, root='./assets/css')

if __name__ == '__main__':
	run(reloader=True, debug=True)

run(host='localhost', port=8000)