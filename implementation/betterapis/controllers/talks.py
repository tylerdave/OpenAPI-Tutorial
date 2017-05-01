import logging
from flask import jsonify, url_for
from betterapis.app import api, db
from betterapis.models import Talk

def get(talk_id):
    # find the talk by id or return a 404
    talk = Talk.query.get_or_404(talk_id)
    return talk.dump()

def post(talk):
    # create a new talk from the post data
    new_talk = Talk(**talk)
    # save the new talk to the database
    db.session.add(new_talk)
    db.session.commit()
    # find the url of the new talk
    new_talk_url = url_for('.betterapis_controllers_talks_get',
            talk_id=new_talk.id)
    # build a 201 Created response with a location header and empty body
    response = jsonify(talk_id=new_talk.id)
    response.status_code = 201
    response.headers = {'Location': new_talk_url}
    return response

def put(talk_id, talk):
    orig_talk = Talk.query.get_or_404(talk_id)
    orig_talk.update(**talk)
    db.session.add(orig_talk)
    db.session.commit()
    updated_talk = Talk.query.get_or_404(talk_id)
    return updated_talk.dump()

def delete(talk_id):
    talk = Talk.query.get_or_404(talk_id)
    db.session.delete(talk)
    db.session.commit()
    return jsonify()

def search():
    talks = Talk.query.all()
    talks_response = [talk.dump() for talk in talks]
    return jsonify(talks_response)
