from utils.database_utils import Base
from sqlalchemy import Column, Integer, String
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = "users"

    id:int = Column(Integer, primary_key=True, index=True)
    user_name:str = Column(String, index=True, unique=True)
    email:str = Column(String, index=True, unique=True)
    hashed_password:str = Column(String) 

    def verify_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)