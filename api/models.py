#db structure
from sqlalchemy import Column,Integer,String
from database import Base

class Users(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)

class WeightData(Base):
    __tablename__='weighbridge'
    id=Column(Integer,primary_key=True,index=True)
    weight=Column(Integer)
    # datetime=Column()
    