from typing import Any, Dict
from datetime import datetime
from database import Base, get_db
from sqlalchemy import Column, INTEGER, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError
from my_project import constants
from logging.config import dictConfig
import logging
from config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("fastapi-project")

session = next(get_db())


class Blog(Base):
    # To change actual table name in the database, As by default it will be same as the model name
    __tablename__ = "blogs"

    blog_id = Column(INTEGER, primary_key=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
    owner_id = Column(INTEGER, ForeignKey("users.user_id", ondelete="CASCADE"))

    owner = relationship("User", back_populates="blogs")

    def __repr__(self):
        return f"< Blog {self.blog_id}>"

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.title = kwargs.get("title")
        self.content = kwargs.get("content")
        self.owner_id = kwargs.get("owner_id")

    def save(self, db):
        db.add(self)
        db.commit()

    @classmethod
    def save_blog(cls, data: Dict):
        try:
            blog = cls(**data)
            blog.save(session)
            session.refresh(blog)
            return blog
        except SQLAlchemyError:
            logger.error(constants.ERR_SQL_ALCHEMY_ERROR)
            return None

    @classmethod
    def get_blog(cls, blog_id: int):
        return session.query(cls).get(blog_id)

    @classmethod
    def check_current_user_blog(cls, blog_id: int, current_user: int):
        return session.query(cls).filter(cls.blog_id == blog_id, cls.owner_id == current_user).first()

    @classmethod
    def delete_blog(cls, blog_id: int, owner_id: int):
        try:
            obj = session.query(cls).filter(cls.blog_id == blog_id, cls.owner_id == owner_id)
            obj.delete()
            session.commit()
            return obj

        except SQLAlchemyError:
            logger.error(constants.ERR_SQL_ALCHEMY_ERROR)
            return None

    @classmethod
    def update_blog_in_db(cls, blog_id: int, data: Dict, owner_id: int):
        try:
            obj = session.query(cls).filter(cls.blog_id == blog_id, cls.owner_id == owner_id)
            obj.update(data)
            session.commit()
            return obj
        except SQLAlchemyError:
            logger.error(constants.ERR_SQL_ALCHEMY_ERROR)
            return None
