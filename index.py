#!/usr/bin/python3
# coding=utf-8

import bottle
import settings
from my_db import Session, ComputerHardware
from bottle import view, request, response, static_file, abort, redirect

app = application = bottle.Bottle()

@app.route(settings.PREFIX + '/')
@view('mainpage')
def main():
    return dict()

if __name__ == '__main__':
    bottle.run(app=app,
        debug=True, reloader=True,
        host='127.0.0.1',
        port=8888)
