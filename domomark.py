import os 
from flask import Flask
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(loader=PackageLoader('domomark','templates'))
template = env.get_template('testone.html')

@app.route('/')
def hello():
    #return 'Hello World!'
    print template.render()