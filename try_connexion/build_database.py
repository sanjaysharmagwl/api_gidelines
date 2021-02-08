import os
from api.schemas.v1._people import Person

from api import create_app

spec   = os.path.join(os.path.abspath(os.path.dirname(__file__)), "openapi")
config = os.path.join(os.path.abspath(os.path.dirname(__file__)), "config","config.py")

application = create_app(spec,config)
db = application.db

# Data to initialize database with
PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny','lname': 'Easter'}
]

# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)

db.session.commit()