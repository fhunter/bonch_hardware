#!/usr/bin/python3
# coding=utf-8

""" Hardware configuration monitoring application """

import datetime
import socket
import bottle
import jsondiff
#from bottle import view, request, response, static_file, abort, redirect
from sqlalchemy import func
from bottle import view, request, abort, static_file, template
from data import filter_hardware_report
import settings
from my_db import Session, ComputerHardware

app = application = bottle.Bottle()

@app.error(404)
def error404(error_m):
    """ Error 404 page """
    return template(
        '404_template',
        refresh = 5,
        url = settings.PREFIX,
        title = "Страница не найдена",
        body = error_m.body)

@app.route(settings.PREFIX + '/')
@view('mainpage')
def main():
    """ Main view page """
    session = Session()
    computers = session.query(
        ComputerHardware.hostname,
        func.max(ComputerHardware.date).label('date'),
        func.count(ComputerHardware.hostname).label('count')
    ).order_by(ComputerHardware.date.desc())
    computers = computers.group_by(ComputerHardware.hostname).\
                order_by(ComputerHardware.date.desc())
    computers=computers.all()
    session.close()
    return dict(computers=computers)

@app.route(settings.PREFIX + r'/img/<filename:re:.*\.svg>')
def send_files(filename):
    """ Static file server """
    return static_file(filename, root='./img/', mimetype='image/svg+xml')

@app.route(settings.PREFIX + '/computer/<name>')
@app.route(settings.PREFIX + '/computer/<name>/<version1:int:[0-9]+>')
@view('computer')
def computerview(name, version1=None):
    """ View computer hardware """
    print(version1)
    session = Session()
    computers = session.query(ComputerHardware).\
        order_by(ComputerHardware.date.desc()).\
        filter(ComputerHardware.hostname == name)
    if version1 is not None:
        # specific version
        computers = computers[version1:version1+1]
    else:
        computers = computers.all()
        version1 = 0
    session.close()
    hostname = ""
    if computers:
        hostname = computers[0].hostname
    else:
        abort(404,f"Компьютер {name} не найден")
    return dict(computers = computers, hostname = hostname, start = version1)

@app.route(settings.PREFIX + '/computer/<name>/<version1:int:[0-9]+>/<version2:int:[0-9]+>')
@view('diffview')
def diffview(name, version1, version2):
    """ View computer hardware """
    print(version1,version2)
    session = Session()
    computers = session.query(ComputerHardware).\
        order_by(ComputerHardware.date.desc()).\
        filter(ComputerHardware.hostname == name)
    # this is diff
    try:
        computer1 = computers[version1]
        computer2 = computers[version2]
    except IndexError:
        abort(404,f"Версии аппаратуры {version1}-{version2} не найдены для {name}")
    session.close()
    hostname = ""
    if computer1 and computer2:
        hostname = computer2.hostname
    else:
        abort(404,f"Компьютер {name} не найден")
    return dict(computer1 = computer1,
                computer2 = computer2,
                hostname = hostname,
                start = version1,
                end = version2)


@app.route(settings.PREFIX + '/data', method='POST')
def post_data():
    """ Data receiver endpoing """
    ip_addr = request.environ.get("REMOTE_ADDR")
    hostname = request.environ.get("REMOTE_HOST")
    if hostname is None:
        hostname = socket.gethostbyaddr(ip_addr)[0]
    if hostname == "":
        hostname = ip_addr
    data = filter_hardware_report(request.json)
    session = Session()
    computer = session.query(ComputerHardware).\
        filter(ComputerHardware.hostname == hostname).\
        order_by(ComputerHardware.date.desc()).limit(1).one()
    if computer:
        #Data is present - compare, then add new
        if jsondiff.diff(computer.hardware, data, syntax='explicit'):
            cdata = ComputerHardware(
                hostname = hostname,
                ip = ip_addr,
                date = datetime.datetime.now(),
                hardware = data)
            session.add(cdata)
    else:
        #Data not present - insert
        cdata = ComputerHardware(
            hostname = hostname,
            ip = ip_addr,
            date = datetime.datetime.now(),
            hardware = data)
        session.add(cdata)
    session.commit()
    session.close()
    return dict()

if __name__ == '__main__':
    bottle.run(app=app,
        debug=True, reloader=True,
        host='127.0.0.1',
        port=8888)
