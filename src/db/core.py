from .models import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import db_url


def init_db(db_url=db_url):
    engine = create_engine(db_url)
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)


def make_session(db_url=db_url):
    engine = create_engine(db_url)
    session = sessionmaker()
    session.configure(bind=engine)
    return session()


