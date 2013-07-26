import os, urllib2
from flask import Flask
from jinja2 import Environment, PackageLoader

app = Flask(__name__)
env = Environment(loader=PackageLoader('domomark','templates'))
template = env.get_template('index.html')

n = 1000000000
outputString = 'Print a Fibonacci series up to %d: ' % n
a, b = 0, 1

def testFib(n):
	global outputString	
	global a, b
	while b<n:
		outputString += '%d, ' % b 
		a, b = b, a+b
	return outputString


@app.route('/')
def hello():
	global n
	testFib(n)
	return outputString
    #return template.render(outputString)
    
    
@app.route('/Test')
def test():
	return "Test Page"
    #return template.render(outputString)
    
@app.route('/Two')
def test2():
    return template.render(title="Project Domomark")