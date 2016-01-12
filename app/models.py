from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Numeric, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationships
from conf.settings import DB_TYPE, DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_NAME

DB_INFO = '%s://%s:%s@%s:%i/%s' % (DB_TYPE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
engine = create_engine(DB_INFO)

Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()  # For view import ...


class PositionTable(Base):
    __tablename__ = 'position_info'

    id = Column(Integer, primary_key=True)
    alarm = Column(Integer)
    status = Column(Integer)
    latitude = Column(Float(9))
    longitude = Column(Float(9))
    altitude = Column(Integer)
    speed = Column(Integer)
    direction = Column(Integer)
    timestamp = Column(Integer)


if __name__ == '__main__':
    pass
