from datetime import datetime
# from ._base import BaseModel , BaseSchema , db
from api.plugins import db, ma

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column('person_id',db.Integer, primary_key=True)
    lname = db.Column('lname',db.String(32), index=True)
    fname = db.Column('fname',db.String(32))
    timestamp = db.Column('timestamp',db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class PersonSchema(db.Model):
    class Meta:
        model = Person