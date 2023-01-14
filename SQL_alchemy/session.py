from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database

engine = create_engine("postgresql://postgres:admin123@localhost/store_2")
# This creates database
if not database_exists(engine.url):
    create_database(engine.url)
__session = sessionmaker(engine, autocommit=True)
session: Session = __session()
