# https://www.youtube.com/watch?v=I6j96qnrbxo

# A Web application that shows Google Maps around schools, using
# the Flash framwork, and the Google Maps API.

from flask import Flask, render_template, abort
# Flask is a microframework for Python based on Werkzeug, Jinja 2 and good ... 
# from flask import Flask app = Flask(__name__) @app.route("/") def hello(): return ...
# install Flask: pip install Flask

# Source Codes at: https://github.com/dcbriccetti/python-lessons/tree/master/Web/flask/gmap

app = Flask(__name__) 

class School: 
    def __init__(self, key, name, lat, lng): 
        self.key  = key 
        self.name = name 
        self.lat  = lat 
        self.lng  = lng 
 
schools = ( 
    School('hv',      'Happy Valley Elementary',   37.9045286, -122.1445772), 
    School('stanley', 'Stanley Middle',            37.8884474, -122.1155922), 
    School('wci',     'Walnut Creek Intermediate', 37.9093673, -122.0580063) 
) 
schools_by_key = {school.key: school for school in schools} 
 
@app.route("/") 
def index(): 
    return render_template('index.html', schools=schools) 
  
@app.route("/<school_code>") 
def show_school(school_code): 
    school = schools_by_key.get(school_code) 
    if school: 
        return render_template('map.html', school=school) 
    else: 
        abort(404) 

 
app.run(host='localhost', debug=True) 
