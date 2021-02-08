from api.plugins import db, ma

class BaseModel(db.Model):
    pass

class BaseSchema(ma.Schema):
    pass