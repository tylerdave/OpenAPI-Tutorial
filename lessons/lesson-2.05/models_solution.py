import arrow
from betterapis import db

class Review(db.Model, SimpleSerializing):
    id = db.Column(db.Integer, primary_key=True)
    talk_id = db.Column(db.Integer)
    details = db.Column(db.String)

    def __init__(self, **kwargs):
        self.talk_id = kwargs.get('talk_id')
        self.details = kwargs.get('details')

    def update(self, **kwargs):
        self.__init__(**kwargs)

    def __repr__(self):
        return '<Review {} {}>'.format(self.talk_id, self.details)
