from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import Department
from .schemas import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

@router.post("/", response_model=DepartmentResponse)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    new_department = Department(**department.model_dump())

    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()


@router.get("/{dept_id}", response_model=DepartmentResponse)
def get_department(
    dept_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(
        Department.dept_id == dept_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.put("/{dept_id}", response_model=DepartmentResponse)
def update_department(
    dept_id: int,
    department_data: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(
        Department.dept_id == dept_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    department.dept_name = department_data.dept_name

    db.commit()
    db.refresh(department)

    return department


@router.delete("/{dept_id}")
def delete_department(
    dept_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(
        Department.dept_id == dept_id
    ).first()

    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    db.delete(department)
    db.commit()

    return {"message": "Department deleted successfully"}