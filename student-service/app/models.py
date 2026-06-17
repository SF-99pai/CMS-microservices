from sqlalchemy import Column, Integer, String
from .database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String, nullable=False)
    dept_id = Column(Integer, nullable=False)