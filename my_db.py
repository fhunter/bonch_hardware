# vim: set fileencoding=utf-8 :
#import secret

""" Database access abstraction module """

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

engine = create_engine('sqlite:///database_.sqlite3', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class ComputerHardware(Base):
    """ SQL table for computer hardware. data field contains json as string """
    __tablename__ = 'computer_hardware'

    id = Column(Integer, primary_key=True)
    machineid = Column(String, nullable = False)
    hostname = Column(String, nullable = False)
    ip = Column(String, nullable = False)
    date = Column(DateTime, nullable = False, default=func.now())
    hardware = Column(String, nullable = False)

    def __repr__(self):
        tmpl = "<Computer(hostname='%s' machineid='%s' "
        tmpl = tmpl + "date='%s' ip='%s' hardware='%s')>"
        return tmpl % (
            self.hostname, self.machineid, self.date, self.ip, self.hardware)

Base.metadata.create_all(engine)
