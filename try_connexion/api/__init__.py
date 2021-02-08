import os
import connexion
from .plugins import db, ma

def create_app(spec=None, config=None):
    
    connex_app = connexion.App(
        __name__,
        specification_dir=spec,
        options={"swagger_ui": False, "serve_spec": False},
    )
   
    connex_app.add_api("v1.yml", strict_validation=True)
    
    flask_app = connex_app.app

    if config is None:
        config = os.path.join(flask_app.root_path, os.environ.get('FLASK_APPLICATION_SETTINGS'))
    
    flask_app.config.from_pyfile(config)
    
    #initalize plugins
    db.init_app(flask_app)
    ma.init_app(flask_app)

    #import routes       
    from .resources import v1       
        
    # Register Blueprints ...

    return flask_app