import sqlite3
import random
from flask import Flask, render_template, g
app = Flask(__name__)

@app.route('/')
def index():
    data = get_db()
    return render_template("index.html", all_data = data)  
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database/Sensor.db')                
        cursor = db.cursor()
        cursor.execute("select * from sensordata")
        all_data = cursor.fetchall()
    return all_data
if __name__ == '__main__':
    app.run()
    
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if name == 'main':
    app.run()