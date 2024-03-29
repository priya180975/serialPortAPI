#config for database

from sqlalchemy import create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite:/// data.db"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False}
)

#create session
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

#connect to db instance via session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()