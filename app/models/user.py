from sqlalchemy import Column, Integer, String
from app.crud.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    role_type = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)