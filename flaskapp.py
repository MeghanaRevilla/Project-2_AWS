import sqlite3

from flask import Flask, request, g, render_template, send_file

DATABASE = '/var/www/html/flaskapp/example.db'
#DATABASE = 'C:/Users/karan/OneDrive/Documents/AWS folder cloud/example.db'
app = Flask(__name__)
app.config.from_object(__name__)

def connect_to_database():
    # return sqlite3.connect(app.config['DATABASE'])
    return sqlite3.connect(DATABASE)

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()