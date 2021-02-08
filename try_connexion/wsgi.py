import os
from api import create_app

spec   = os.path.join(os.path.abspath(os.path.dirname(__file__)), "openapi")
config = os.path.join(os.path.abspath(os.path.dirname(__file__)), "config","config.py")

application = create_app(spec,config)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000, debug=True)