# This is a simple example web app that is meant to illustrate the basics.
from flask import Flask, render_template, redirect, g, request, url_for
import sqlite3

DATABASE = 'todolist.db'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def show_list():
	with urllib.request.urlopen('http://localhost:5000/api/items') as response:
		resp = response.read()
	resp = json.loads(resp)
	return render_template('index.html', todolist=resp)


@app.route("/add", methods=['POST'])
def add_entry():
	with urllib.request.urlopen('http://localhost:5000/api/items/add') as response:
		resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/delete/<item>")
def delete_entry(item):
	with urllib.request.urlopen('http://localhost:5000/api/items/delete/<item>') as response:
		resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))


@app.route("/mark/<item>")
def mark_as_done(item):
	with urllib.request.urlopen('http://localhost:5000/api/items/mark/<item>') as response:
		resp = response.read()
	resp = json.loads(resp)
	return redirect(url_for('show_list'))

if __name__ == "__main__":
	app.run("0.0.0.0")
