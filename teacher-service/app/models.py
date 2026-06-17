from sqlalchemy import Column, Integer, String
from .database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    teacher_name = Column(String, nullable=False)
    dept_id = Column(Integer, nullable=False)