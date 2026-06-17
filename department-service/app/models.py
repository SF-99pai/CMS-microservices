from sqlalchemy import Column, Integer, String
from .database import Base

class Department(Base):
    __tablename__ = "deptartments"

    dept_id = Column(Integer, primary_key=True, index=True)
    dept_name = Column(String, nullable=False)