"""
REST API Microservice Example
Name: Mike Weiss
Email: blackdog.gianttree@gmail.com
"""

from flask import Flask, abort, jsonify, request

API_VER = 'v1.0'

API = Flask(__name__)
DB = {}


@API.route('/api/'+API_VER+'/key', methods=['POST'])
def add_key():
    """ Add key / value pair """
    try:
        key, value = request.json['key'], request.json['value']
    except StandardError:
        abort(400)
    DB[key] = value
    return jsonify({key: DB[key]}), 201


@API.route('/api/'+API_VER+'/key/<string:key>', methods=['GET'])
def get_key(key):
    """ Get key / value pair """
    try:
        DB[key]
    except StandardError:
        abort(404)
    return jsonify({key: DB[key]}), 200


@API.route('/api/'+API_VER+'/key/<string:key>', methods=['PUT'])
def update_key(key):
    """ Update key / value pair """
    try:
        value = request.json['value']
    except StandardError:
        abort(400)
    DB[key] = value
    return jsonify({key: DB[key]}), 201


@API.route('/api/'+API_VER+'/key/<string:key>', methods=['DELETE'])
def delete_key(key):
    """ Delete key / value pair """
    try:
        DB.pop(key)
    except KeyError:
        abort(400)
    return jsonify({'result': True}), 202


@API.route('/api/'+API_VER+'/key', methods=['GET'])
def get_all_keys():
    """ Get all key / value pairs """
    try:
        DB
    except NameError:
        abort(404)
    return jsonify({'keys': DB}), 200


@API.errorhandler(404)
@API.errorhandler(400)
def report_bad(error):
    """ Handle adds, gets, updates and deletes; return JSON error """
    return jsonify({'error': error.code}), error.code


@API.errorhandler(Exception)
def report_general_error(error):
    """ Handle miscelaneous errors; return JSON error """
    print error
    return jsonify({'error': 500}), 500


if __name__ == '__main__':
    API.run(host='0.0.0.0')
