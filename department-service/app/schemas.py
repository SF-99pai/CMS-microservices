from pydantic import BaseModel

class DepartmentCreate(BaseModel):
    dept_name: str

class DepartmentUpdate(BaseModel):
    dept_name: str

class DepartmentResponse(BaseModel):
    dept_id: int
    dept_name: str

    class Config:
        from_attributes = True