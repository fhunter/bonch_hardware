#!/usr/bin/python3
# coding=utf-8

""" Hardware configuration monitoring application """

import datetime
import socket
import bottle
#from bottle import view, request, response, static_file, abort, redirect
from sqlalchemy import or_, func
from bottle import view, request, abort, static_file
import settings
from my_db import Session, ComputerHardware

app = application = bottle.Bottle()

@app.error(404)
def error404(error_m):
    e_message = "<html><head>"
    e_message += f"<meta http-equiv=\"refresh\" content=\"5; url='{settings.PREFIX}/'\" />"
    e_message += "</head><body><h1>Страница не найдена</h1></body></html>"
    return e_message

@app.route(settings.PREFIX + '/')
@view('mainpage')
def main():
    """ Main view page """
    session = Session()
    computers = session.query(
        ComputerHardware.hostname,
        ComputerHardware.date,
        func.count(ComputerHardware.hostname).label('count')
    ).group_by(ComputerHardware.hostname).order_by(ComputerHardware.date).all()
    session.close()
    return dict(computers=computers)

@app.route(settings.PREFIX + r'/img/<filename:re:.*\.svg>')
def send_files(filename):
    return static_file(filename, root='./img/', mimetype='image/svg+xml')

@app.route(settings.PREFIX + '/computer/<name>')
@view('computer')
def computerview(name):
    """ View computer hardware """
    session = Session()
    computers = session.query(ComputerHardware).\
        group_by(ComputerHardware.hostname).\
        filter(ComputerHardware.hostname == name).\
        order_by(ComputerHardware.date).all()
    session.close()
    hostname = ""
    if computers:
        hostname = computers[0].hostname
    else:
        abort(404,"Not found")
    return dict(computers = computers, hostname = hostname)

@app.route(settings.PREFIX + '/data', method='POST')
def post_data():
    """ Data receiver endpoing """
    ip_addr = request.environ.get("REMOTE_ADDR")
    hostname = request.environ.get("REMOTE_HOST")
    if hostname is None:
        hostname = socket.gethostbyaddr(ip_addr)[0]
    if hostname == "":
        hostname = ip_addr
    data = request.json
    session = Session()
    computer = session.query(ComputerHardware).filter(ComputerHardware.hostname == hostname).order_by(ComputerHardware.date.desc()).limit(1).all()
    if computer:
        #Data is present - compare, then update
        computer[0].date = datetime.datetime.now()
        computer[0].hardware = data
        computer[0].ip = ip_addr
    else:
        #Data not present - insert
        cdata = ComputerHardware(hostname = hostname, ip = ip_addr, date = datetime.datetime.now(), hardware = data)
        session.add(cdata)
    session.commit()
    session.close()
    return dict()

if __name__ == '__main__':
    bottle.run(app=app,
        debug=True, reloader=True,
        host='127.0.0.1',
        port=8888)
