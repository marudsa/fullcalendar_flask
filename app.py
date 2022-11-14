from turtle import title
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import *
from sqlalchemy import *
from models.calendar_model import *
from utils.db import db
from datetime import *
from models.calendar_model import Calendar

app = Flask(__name__)

app.secret_key = "caircocoders-ed"

host = "localhost"
database = "testingdb"
user = "root"
password = "root"

app.config['SQLALCHEMY_DATABASE_URI'] =  f'mysql://{user}:{password}@{host}:33061/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

@app.route('/')
def index():
    calendar = Calendar.query.all()
    return render_template('calendario.html', calendar=calendar)

@app.route("/insert",methods=["POST","GET"])
def insert():
    #msg = 'success'
    #return jsonify(msg)
    if request.method == "POST":
        title = request.form["title"]
        start = request.form["start"]
        start = datetime.strptime(start, '%Y/%m/%d %H:%M:%S')
        end = request.form["end"]
        end = datetime.strptime(end, '%Y/%m/%d %H:%M:%S')
        
        new_event = Calendar(title, start, end)
        db.session.add(new_event)
        db.session.commit()
        msg = "success"
    return jsonify(msg)

@app.route("/update", methods=["POST","GET"])
def update():
    id = int(request.form["id"])
    eventscalendar = Calendar.query.get(id)
    if request.method == "POST":
        start = request.form["start"]
        end = request.form["end"]
        start = datetime.strptime(start, '%Y/%m/%d %H:%M:%S')
        print(start)
        end = datetime.strptime(end, '%Y/%m/%d %H:%M:%S')
        print(end)
        title = request.form["title"]
        print(title)
        eventscalendar.title = title
        eventscalendar.start_event = start
        eventscalendar.end_event = end
        
        db.session.commit()
        
        msg = "success"
    return jsonify(msg)

@app.route("/ajax_delete", methods=["POST","GET"])
def ajax_delete():
    id = int(request.form["id"])
    eventscalendar = Calendar.query.get(id)
    if request.method == "POST":
        db.session.delete(eventscalendar)
        db.session.commit()
        
        msg = "Record deleted successfully"
    return jsonify(msg)