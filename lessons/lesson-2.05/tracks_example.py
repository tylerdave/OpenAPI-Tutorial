from flask import jsonify, url_for
from betterapis.app import api, db
from betterapis.models import Track

def get(track_id):
    # find the review by id or return a 404
    track = Track.query.get_or_404(track_id)
    return track.dump()

def post(track):
    # create a new review from the post data
    new_track = Track(**track)
    # save the new review to the database
    db.session.add(new_track)
    db.session.commit()
    response = jsonify(track_id=new_track.id)
    response.status_code = 201
    return response
