from typing import Any

from datetime import datetime
from database import Base, get_db
from sqlalchemy import Column, INTEGER, String, DateTime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from my_project import constants
from logging.config import dictConfig
import logging
from config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("fastapi-project")

session = next(get_db())


class User(Base):
    # To change actual table name in the database, As by default it will be same as the model name
    __tablename__ = 'users'

    user_id = Column(INTEGER, primary_key=True)
    user_name = Column(String(30), nullable=False, unique=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(200), nullable=False)
    email = Column(String(62), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())

    blogs = relationship("Blog", back_populates="owner")

    def __repr__(self):
        return f"< User {self.user_id}>"

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.user_name = kwargs.get("user_name")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def save(self, db):
        db.add(self)
        db.commit()

    @classmethod
    def get_user(cls, user_id):
        return session.query(cls).get(user_id)

    @classmethod
    def check_is_username_exists(cls,
                                 username):
        return session.query(cls).filter(cls.user_name == username).first()

    @classmethod
    def check_is_email_exists(cls, email):
        return session.query(cls).filter(cls.email == email).first()

    @classmethod
    def save_user(cls, data):
        try:
            user = cls(**data)
            user.save(session)
            session.refresh(user)
            return user
        except SQLAlchemyError:
            logger.error(constants.ERR_SQL_ALCHEMY_ERROR)
            return None

    @classmethod
    def update_password(cls, current_user, password):
        try:
            obj = session.query(cls).filter(cls.user_id == current_user, ).first()
            obj.password = password
            session.commit()
            return obj
        except SQLAlchemyError:
            logger.error(constants.ERR_SQL_ALCHEMY_ERROR)
            return None
