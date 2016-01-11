from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Numeric, String, Integer,ForeignKey
from sqlalchemy.orm import relationships


engine = create_engine('mysql://root:tianxunceshi@localhost:3306/sqlalchemy_demo')
# engine = create_engine("mysql:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# class Cookie(Base):
#     __tablename__ = 'cookie'
#
#     cookie_id = Column(Integer, primary_key=True)
#     cookie_name = Column(String(50), index=True)
#     cookie_recipe_url = Column(String(255))
#     cookie_sku = Column(String(55))
#     quantify = Column(Integer())
#     unit_cost = Column(Numeric(12, 2))

class PositionTable(Base):
    __tablename__ = 'position_info'

    alarm = Column(Integer)
    status = Column(Integer)
    latitude = Column(Integer)
    longitude = Column(Integer)
    altitude = Column(Integer)
    speed = Column(Integer)
    direction = Column(Integer)
    timestamp = Column(Integer)


Base.metadata.create_all(engine)

if __name__ == '__main__':
    # cc_cookie = Cookie(cookie_name='google',
    #                    cookie_recipe_url='www.google.com',
    #                    cookie_sku='cc01',
    #                    quantify=12,
    #                    unit_cost=0.50)
    # session.add(cc_cookie)
    # session.commit()
    # print cc_cookie.cookie_id
    # print cc_cookie.cookie_name
    # cookies = session.query(Cookie).all()
    # print cookies
    pass