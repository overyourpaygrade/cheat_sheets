#!/usr/bin/env python

import sqlite3
from flask import Flask, request, g, redirect, url_for, render_template, abort, jsonify
from contextlib import closing
import index 

# Declare config
DATABASE = './api.db'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# Connect to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

# Initialize the database
def init_db():
	with closing(connect_db()) as db:
		with app.open_resource('./schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

@app.before_request
def before_request():
	g.db = connect_db();

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

# TLD
@app.route('/')
def get_posts():
	cur = g.db.execute('select title, text from posts order by id asc')
	posts = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('show_posts.html', posts=posts)

@app.route('/api/v1/posts/', methods=['GET'])
def show_entries():
	cur = g.db.execute('select title, text from posts order by id asc')
	posts = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return jsonify({'count': len(posts), 'posts': posts})

@app.route('/api/v1/posts/<int:post_id>', methods=['GET', 'DELETE'])
def single_post(post_id):
	method = request.method
	if method == 'GET':
		cur = g.db.execute('select title, text from posts where id=?', [post_id])
		posts = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
		return jsonify({'count': len(posts), 'posts': posts})
	elif method == 'DELETE':
		g.db.execute('delete from posts where id=' + str(post_id))
		g.db.commit()
		return jsonify({'status': 'Post deleted'})
	

# Add methods and routes here
if __name__ == '__main__':
	init_db()
	app.run()
