# -*- coding: utf-8 -*-

import os
import sqlite3
import time
from jinja2 import Environment, PackageLoader
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack
    
app = Flask(__name__)
env = Environment(loader=PackageLoader('domomark','templates'))
template = env.get_template('index.html')

class User(object):
	username = ""
	password = ""
	firstname = ""
	lastname = ""
	lastLoggedOn = ""
	logonTime = ""
	createdOn = ""

user = User()

# Validate Login Credentials
# TODO: Link into a Database
# TODO: Encrypt the username and password
def validateLogin(loginUsername,loginPassword):
	if(loginUsername=='ML' and loginPassword=='ML'):
		user.username = loginUsername
		user.password = loginPassword
		return True
	else:
		return False

@app.route('/',methods=['GET','POST'])
def main():
	# Already logged in
	if user.username != "":
		return template.render(title="Project Domomark", alerts="Welcome back %s. You last logged on at %s" % (user.username, user.lastLoggedOn))
		
	# Not logged in yet
	if request.method == 'GET':
		return template.render(title="Project Domomark", alerts="Welcome to the homepage")
	else:
		if validateLogin(request.form['username'],request.form['password']):
			user.lastLoggedOn = user.logonTime
			user.logonTime = time.strftime('%l:%M%p on %b %d, %Y')
			return template.render(title="Project Domomark", alerts="Welcome back %s. You last logged on at %s" % (user.username, user.lastLoggedOn))
		else:
			return template.render(title="Project Domomark", alerts="This is an INVALID login request")

@app.route('/register')
def register():
	return template.render(title="Project Domomark", alerts="Welcome back %s. You last logged on at %s" % (user.username, user.lastLoggedOn))

@app.route('/logout')
def logout():
	user.username = ""
	user.password = ""
	return redirect(url_for('main', title="Project Domomark", alerts="Logged Out Successfully"))
	#return template.render(title="Project Domomark", alerts="Logged Out Successfully")


@app.route('/about')
def about():
	return template.render(title="Project Domomark", alerts="This is the about page")

# Initialize program
if __name__ == '__main__':
	app.debug = True
	app.run()
