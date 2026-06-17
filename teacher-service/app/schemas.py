from pydantic import BaseModel

class TeacherCreate(BaseModel):
    teacher_name: str
    dept_id: int


class TeacherUpdate(BaseModel):
    teacher_name: str
    dept_id: int


class TeacherResponse(BaseModel):
    teacher_id: int
    teacher_name: str
    dept_id: int

    class Config:
        from_attributes = True