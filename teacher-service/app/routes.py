from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import Teacher
from .schemas import (
    TeacherCreate,
    TeacherUpdate,
    TeacherResponse
)

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)

@router.post("/", response_model=TeacherResponse)
def create_teacher(
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):
    new_teacher = Teacher(**teacher.model_dump())

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher


@router.get("/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()


@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher


@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher(
    teacher_id: int,
    teacher_data: TeacherUpdate,
    db: Session = Depends(get_db)
):
    teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    teacher.teacher_name = teacher_data.teacher_name
    teacher.dept_id = teacher_data.dept_id

    db.commit()
    db.refresh(teacher)

    return teacher


@router.delete("/{teacher_id}")
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    db.delete(teacher)
    db.commit()

    return {"message": "Teacher deleted successfully"}