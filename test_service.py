"""
Test REST API Microservice Example
Name: Mike Weiss
Email: michaelthomasweiss@gmail.com
"""

import json
import requests

HEADERS = {'Content-type': 'application/json'}
BASE_URL = 'http://127.0.0.1:5000/api/v1.0/key'


def test_add_key1():
    """ Test1 add key / value pair """
    payload = {'key': 'foo', 'value': 'bar'}
    requests.post(BASE_URL, data=json.dumps(payload), headers=HEADERS)


def test_get_key1():
    """ Test1 get key / value pair """
    req = requests.get(BASE_URL+'/foo', headers=HEADERS)
    assert req.json()['foo'] == 'bar'


def test_add_key2():
    """ Test2 add key / value pair """
    payload = {'key': 'sports', 'value': 'baseball'}
    requests.post(BASE_URL, data=json.dumps(payload), headers=HEADERS)


def test_update_key2():
    """ Test2 modify key / value pair """
    payload = {'value': ['baseball', 'hockey', 'football']}
    requests.put(BASE_URL+'/sports', data=json.dumps(payload), headers=HEADERS)


def test_get_allkeys():
    """ Test get ALL key / value pairs """
    requests.get(BASE_URL, headers=HEADERS)


def test_delete_key1():
    """ Test1 delete key / value pair """
    req = requests.delete(BASE_URL+'/foo', headers=HEADERS)
    assert req.json()['result'] is True


def test_addbad_key():
    """ Test add bad key """
    payload = 'bar'
    req = requests.post(BASE_URL, data=json.dumps(payload), headers=HEADERS)
    assert req.json()['error'] == 400


def test_getbad_key():
    """ Test get bad key """
    req = requests.get(BASE_URL+'/sportsing', headers=HEADERS)
    assert req.json()['error'] == 404
