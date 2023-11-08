# Alley Chaggar 

from flask import Flask;

app = Flask(__name__)

def foo():
    pass

def students():
    return 'Alley Brandon Charlie'

@app.route('/', methods = ['GET'])
def any_function():
    return students()

app.run(debug = True)