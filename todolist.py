# This is a simple example web app that is meant to illustrate the basics.
from flask import Flask, render_template, redirect, g, request, url_for
import sqlite3
import json
from urllib2 import urlopen, Request
import urllib
import os

DATABASE = 'todolist.db'

app = Flask(__name__)
app.config.from_object(__name__)
print(dir(os.environ))

TODO_API_URL = os.environ['TODO_API_IP']+":5000"
print(TODO_API_URL)
@app.route("/")
def show_list():
	response = urlopen(TODO_API_URL+'/api/items')
	resp = response.read()
	resp = json.loads(resp)
	return render_template('index.html', todolist=resp)


@app.route("/add", methods=['POST'])
def add_entry():
	print(request.form['what_to_do'])
	print(request.form['due_date'])
	dataz = json.dumps({'whatToDo': request.form['what_to_do'], 'dueDate': request.form['due_date']})
	req = Request(TODO_API_URL+'/api/items/add', data=dataz, headers={'Content-Type': 'application/json'})
	response = urlopen(req)
	resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
	response = urlopen(TODO_API_URL+'/api/items/delete/'+urllib.quote_plus(item))
	resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/mark/<item>")
def mark_as_done(item):
	response = urlopen(TODO_API_URL+'/api/items/mark/'+urllib.quote_plus(item))
	resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))

if __name__ == "__main__":
	app.run("0.0.0.0")
