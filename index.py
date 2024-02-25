#!/usr/bin/python3
# coding=utf-8

""" Hardware configuration monitoring application """

import bottle
#from bottle import view, request, response, static_file, abort, redirect
from bottle import view
import settings
from my_db import Session, ComputerHardware

app = application = bottle.Bottle()

@app.route(settings.PREFIX + '/')
@view('mainpage')
def main():
    """ Main view page """
    return dict()

@app.route(settings.PREFIX + '/data', method='POST')
def post_data():
    """ Data receiver endpoing """
    session = Session()
    session.close()
    return dict()

if __name__ == '__main__':
    bottle.run(app=app,
        debug=True, reloader=True,
        host='127.0.0.1',
        port=8888)
