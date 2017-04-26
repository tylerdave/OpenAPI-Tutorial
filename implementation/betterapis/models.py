import arrow
from betterapis.app import db

class SimpleSerializing(object):
    """ A mixin to provide simple serialized output """

    def dump(self):
        return {k: v for k, v in vars(self).items() if not k.startswith('_')}


class Talk(db.Model, SimpleSerializing):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    speaker_id = db.Column(db.Integer)
    speaker_id = db.Column(db.Integer, db.ForeignKey('speaker.id'))
    abstract = db.Column(db.String)
    duration = db.Column(db.Integer)
    comments = db.Column(db.String)
    scheduled_on = db.Column(db.DateTime)

    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.speaker_id = kwargs.get('speaker_id')
        self.abstract = kwargs.get('abstract')
        self.duration = kwargs.get('duration')
        self.comments = kwargs.get('comments')
        scheduled_on = kwargs.get('scheduled_on')
        if scheduled_on is not None:
            self.scheduled_on = arrow.get(scheduled_on).datetime
        else:
            self.scheduled_on = None

    def update(self, **kwargs):
        self.__init__(**kwargs)

    def __repr__(self):
        return '<Talk {}>'.format(self.title)


class Speaker(db.Model, SimpleSerializing):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    comments = db.Column(db.String)

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.comments = kwargs.get('comments')

    def update(self, **kwargs):
        self.__init__(**kwargs)

    def __repr__(self):
        return '<Speaker {} {}>'.format(self.first_name, self.last_name)
