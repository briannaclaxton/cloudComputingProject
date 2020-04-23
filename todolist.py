# This is a simple example web app that is meant to illustrate the basics.
from flask import Flask, render_template, redirect, g, request, url_for
import sqlite3
import json
from urllib2 import urlopen, Request
import urllib

DATABASE = 'todolist.db'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def show_list():
	response = urlopen('http://35.223.88.52:5000/api/items')
	resp = response.read()
	resp = json.loads(resp)
	return render_template('index.html', todolist=resp)


@app.route("/add", methods=['POST'])
def add_entry():
	print(request.form['what_to_do'])
	print(request.form['due_date'])
	dataz = json.dumps({'whatToDo': request.form['what_to_do'], 'dueDate': request.form['due_date']})
	req = Request('http://35.223.88.52:5000/api/items/add', data=dataz, headers={'Content-Type': 'application/json'})
	response = urlopen(req)
	resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
	response = urlopen('http://35.223.88.52:5000/api/items/delete/'+unicode(item, 'UTF-8'))
	resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/mark/<item>")
def mark_as_done(item):
	response = urlopen('http://35.223.88.52:5000/api/items/mark/'+item.encode('UTF-8'))
	resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))

if __name__ == "__main__":
	app.run("0.0.0.0")
