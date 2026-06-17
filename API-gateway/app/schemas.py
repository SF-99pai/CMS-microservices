
from pydantic import BaseModel


class StudentCreate(BaseModel):
    student_name: str
    dept_id: int

class TeacherCreate(BaseModel):
    teacher_name: str
    dept_id: int

class DepartmentCreate(BaseModel):
    department_name: str
   


