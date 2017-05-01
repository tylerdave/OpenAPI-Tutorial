from flask import jsonify, url_for
from betterapis import api, db
from betterapis.models import Review

def get(review_id):
    # find the review by id or return a 404
    review = Review.query.get_or_404(review_id)
    return review.dump()

def post(review):
    # create a new review from the post data
    new_review = Review(**review)
    # save the new talk to the database
    db.session.add(new_review)
    db.session.commit()
    # build a 201 Created response with a location header and empty body
    response = jsonify(review_id=new_review.id)
    response.status_code = 201
    return response
