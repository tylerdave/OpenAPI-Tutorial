import arrow
from betterapis import db

class Track(db.Model, SimpleSerializing):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    details = db.Column(db.String)

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.details = kwargs.get('details')

    def update(self, **kwargs):
        self.__init__(**kwargs)

    def __repr__(self):
        return '<Review {} {}>'.format(self.name, self.details)
