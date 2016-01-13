from conf.settings import DB_TYPE, DB_HOST, DB_USER, DB_PASSWORD, DB_PORT, DB_NAME
from visual.visual_decorator import error, info

try:
    import MySQLdb

    DB_INFO = '%s://%s:%s@%s:%i/%s' % (DB_TYPE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
except ImportError, msg:
    error(msg)
    info_msg = "Run 'sudo apt-get install mysql-python' to fixed this!"
    info(info_msg)
    DB_INFO = 'sqlite:///:memory:'

try:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Numeric, String, Integer, ForeignKey, Float
    from sqlalchemy.orm import relationships

    engine = create_engine(DB_INFO)
    Base = declarative_base()
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()  # For view import ...

except ImportError, msg:
    error(msg)
    info_msg = "Run 'pip install sqlalchemy' to fixed this!"
    info(info_msg)

class TerminalTable(Base):
    """
    For save terminal information,if you install the terminal on your car
    there are should be have something like 'car color,car type ,stuff ,etc'
    """
    __tablename__ = 'terminal_info'
    id = Column(Integer,primary_key=True)
    dev_id = Column(String(16))
    dev_color = Column(String(16))


class AuthTable(Base):
    """
    Save the Auth information
    """
    __tablename__ = 'auth_info'

    id = Column(Integer, primary_key=True)
    #dev_id = ForeignKey()
    auth_code = Column(Integer)



class PositionTable(Base):
    """
    Here is ORM framework ,As the below show.
    each field reflect to your data base!
    """
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
    x = PositionTable()
