from fastapi import APIRouter
from pydantic import BaseModel
import httpx

router = APIRouter()

STUDENT_URL = "http://localhost:8001"
TEACHER_URL = "http://localhost:8002"
DEPARTMENT_URL = "http://localhost:8003"


class StudentCreate(BaseModel):
    student_name: str
    dept_id: int


class TeacherCreate(BaseModel):
    teacher_name: str
    dept_id: int


class DepartmentCreate(BaseModel):
    dept_name: str


@router.get("/", tags=["API Gateway"])
def home():
    return {
        "message": "API Gateway Running",
        "services_endpoint": "/services"
    }


@router.get("/services", tags=["API Gateway"])
def services():
    return {
        "available_services": [
            {"service": "Student Service", "endpoint": "/students"},
            {"service": "Teacher Service", "endpoint": "/teachers"},
            {"service": "Department Service", "endpoint": "/departments"}
        ]
    }


# Student Service
@router.get("/students", tags=["Student Service"])
async def get_students():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{STUDENT_URL}/students/")
    return response.json()


@router.post("/students", tags=["Student Service"])
async def create_student(student: StudentCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{STUDENT_URL}/students/",
            json=student.model_dump()
        )
    return response.json()

@router.put("/students/{student_id}", tags=["Student Service"])
async def update_student(student_id: int, student: StudentCreate):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{STUDENT_URL}/students/{student_id}",
            json=student.model_dump()
        )
    return response.json()

@router.delete("/students/{student_id}", tags=["Student Service"])
async def delete_student(student_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{STUDENT_URL}/students/{student_id}"
        )
    return response.json()


# Teacher Service
@router.get("/teachers", tags=["Teacher Service"])
async def get_teachers():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TEACHER_URL}/teachers/")
    return response.json()


@router.post("/teachers", tags=["Teacher Service"])
async def create_teacher(teacher: TeacherCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{TEACHER_URL}/teachers/",
            json=teacher.model_dump()
        )
    return response.json()

@router.put("/teachers/{teacher_id}", tags=["Teacher Service"])
async def update_teacher(teacher_id: int, teacher: TeacherCreate):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{TEACHER_URL}/teachers/{teacher_id}",
            json=teacher.model_dump()
        )
    return response.json()

@router.delete("/teachers/{teacher_id}", tags=["Teacher Service"])
async def delete_teacher(teacher_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{TEACHER_URL}/teachers/{teacher_id}"
        )
    return response.json()


# Department Service
@router.get("/departments", tags=["Department Service"])
async def get_departments():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{DEPARTMENT_URL}/departments/")
    return response.json()


@router.post("/departments", tags=["Department Service"])
async def create_department(department: DepartmentCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{DEPARTMENT_URL}/departments/",
            json=department.model_dump()
        )
    return response.json()

@router.put("/departments/{department_id}", tags=["Department Service"])
async def update_department(department_id: int, department: DepartmentCreate):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{DEPARTMENT_URL}/departments/{department_id}",
            json=department.model_dump()
        )
    return response.json()

@router.delete("/departments/{department_id}", tags=["Department Service"])
async def delete_department(department_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{DEPARTMENT_URL}/departments/{department_id}"
        )
    return response.json()