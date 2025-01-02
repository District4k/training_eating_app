from sqlalchemy import Column, Boolean, Integer, Text, String

from models.base import Base


class UserModel(Base):
    __tablename__ = 'user_model'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    terms = Column(Boolean, nullable=False, default=False)
    sectors = Column(Text, nullable=False)
