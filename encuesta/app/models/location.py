from .. import db

class Location(db.Model):
    __tablename__ = 'location'
    code = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(100))
    parent_code = db.Column(db.String(6))
