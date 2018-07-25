from bottle import route, run, template
#or from bottle import *

#Bottle is a fast, simple and lightweight WSGI micro web-framework for Python
#install bottle: pip install bottle 

HOST = "localhost"

@route('/')
def main():
   return "This is a test"
run(host = HOST, port = 8080, debug = 'true')

#@route('/hello/<name>')
#def index(name):
#    return template('<b>Hello {{name}}</b>!', name=name)

#run(host='localhost', port=8080)