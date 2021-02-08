import os

SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")

baseDir = os.path.abspath(os.path.dirname(__file__))

# Configure the SQLAlchemy part of the app instance
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(baseDir, 'people.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False


