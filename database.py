from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser
import config
from config import Settings

""" DATABASE SETTINGS
---------------------------------------------------------------------------
   The whole database setting can be divided in below stape.

  >>>> https://docs.sqlalchemy.org/en/
   1) set the current server config.
   2) create the sqlalchemy engine.
   3) create the session marker object.
   4) define the declarative base.

   For setting the current server database url on alembic.ini file we need to use configparser python package
   >>> https://stackoverflow.com/questions/8884188/how-to-read-and-write-ini-file-with-python3
   1) create the configparser instance.
   2) read the alembic.ini file.
   3) update the sqlalchemy.url variable.
"""

settings = config.get_current_server_config()

SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=Settings().AUTOCOMMIT, autoflush=Settings().AUTOFLUSH, bind=engine)

Base = declarative_base()

# instantiate
config = ConfigParser()

# parse existing file
config.read('alembic.ini')

# update existing value
config.set('alembic', 'sqlalchemy.url', SQLALCHEMY_DATABASE_URL)


def get_db():
    """
    This method is used to create the database instance.
    :return: database instance
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
