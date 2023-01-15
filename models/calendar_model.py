from utils.db import db
from sqlalchemy.sql import *

class Calendar(db.Model):
    __tablename__ = 'events'
    def __init__(self, title, start_event, end_event):
        self.title = title
        self.start_event = start_event
        self.end_event = end_event
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    start_event = db.Column(db.DateTime)
    end_event = db.Column(db.DateTime)