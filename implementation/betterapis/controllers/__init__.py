from flask import jsonify, url_for
from betterapis.app import api


def get():
    # Get all of the mapped 'search' endpoints and list them as links
    links = {rule.rule.lstrip('/'): url_for(rule.endpoint, _external=True) \
                for rule in api.app.url_map.iter_rules() \
                if rule.endpoint.endswith('_search')}
    return jsonify(links=links)
