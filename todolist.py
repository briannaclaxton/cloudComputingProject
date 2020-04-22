# This is a simple example web app that is meant to illustrate the basics.
from flask import Flask, render_template, redirect, g, request, url_for
import sqlite3
import json
from urllib2 import urlopen

DATABASE = 'todolist.db'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def show_list():
	with urlopen('http://34.70.152.160:5000/api/items') as response:
		resp = response.read()
	resp = json.loads(resp)
	return render_template('index.html', todolist=resp)


@app.route("/add", methods=['POST'])
def add_entry():
	with urlopen('http://34.70.152.160:5000/api/items/add') as response:
		resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
	with urlopen('http://34.70.152.160:5000/api/items/delete/<item>') as response:
		resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/mark/<item>")
def mark_as_done(item):
	with urlopen('http://34.70.152.160:5000/api/items/mark/<item>') as response:
		resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))

if __name__ == "__main__":
	app.run("0.0.0.0")
