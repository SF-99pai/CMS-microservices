from pydantic import BaseModel

class StudentCreate(BaseModel):
    student_name: str
    dept_id: int

class StudentUpdate(BaseModel):
    student_name: str
    dept_id: int

class StudentResponse(BaseModel):
    student_id: int
    student_name: str
    dept_id: int

    class Config:
        from_attributes = True