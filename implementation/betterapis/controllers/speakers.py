import logging
from flask import jsonify, url_for
from betterapis.app import api, db
from betterapis.models import Speaker

def get(speaker_id):
    # find the speaker by id or return a 404
    speaker = Speaker.query.get_or_404(speaker_id)
    return speaker.dump()

def post(speaker):
    # create a new speaker from the post data
    new_speaker = Speaker(**speaker)
    # save the new speaker to the database
    db.session.add(new_speaker)
    db.session.commit()
    # find the url of the new speaker
    new_speaker_url = url_for('.betterapis_controllers_speakers_get',
            speaker_id=new_speaker.id)
    # build a 201 Created response with a location header and empty body
    response = jsonify(speaker_id=new_speaker.id)
    response.status_code = 201
    response.headers = {'Location': new_speaker_url}
    return response

def put(speaker_id, speaker):
    orig_speaker = Speaker.query.get_or_404(speaker_id)
    orig_speaker.update(**speaker)
    db.session.add(orig_speaker)
    db.session.commit()
    updated_speaker = speaker.query.get_or_404(speaker_id)
    return updated_speaker.dump()

def delete(speaker_id):
    speaker = Speaker.query.get_or_404(speaker_id)
    db.session.delete(speaker)
    db.session.commit()
    return jsonify()

def search():
    speakers = Speaker.query.all()
    speakers_response = [speaker.dump() for speaker in speakers]
    return jsonify(speakers_response)
