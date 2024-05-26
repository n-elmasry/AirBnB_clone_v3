#!/usr/bin/python3
""" view for State objects that handles all default RESTFul API actions"""
from models import storage
from models.state import State
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state_list():
    """Retrieves the list of all State objects"""
    states = storage.all(State).values()
    state_list = [state.to_dict() for state in states]
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state_object(state_id):
    """Retrieves a State object"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get('State', state_id)
    if not state:
        abort(404)

    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    data = request.get_json()
    if not data:
        return jsonify(error='Not a JSON'), 400
    if 'name' not in data:
        return jsonify(error='Missing name'), 400
    new = State(**data)
    new.save()

    return jsonify(new.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    """Updates a State"""
    state = storage.get('State', state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify(error='Not a JSON'), 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
