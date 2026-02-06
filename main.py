from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
students_db = {}

class Students(BaseModel):
    name: str
    email:str
    roll_number:str
    department:str

class StudentResponse(BaseModel):
    id:int
    name:str
    email:str
    roll_number:int
    department:str

@app.get("/")
def read_root():
    return {"Hello": "World"}

def create_student(student: Students):
    return student

def read_student(id: int):
    if id in students_db:
        return StudentResponse(id=id, **students_db[id].dict())
    return {"error": "Student not found"}

def update_student(id: int, student: Students):
    students_db[id] = student
    return StudentResponse(id=id, **student.dict())

def delete_student(id: int):
    if id in students_db:
        deleted = students_db.pop(id)
        return StudentResponse(id=id, **deleted.dict())
    return {"error": "Student not found"}

@app.post("/Students")
def create_Student(student: Students):
    student_id = len(students_db) + 1
    students_db[student_id] = student
    return StudentResponse(id=student_id, **student.dict())

@app.get("/Students/{id}")
def read_Student(id: int):
    return read_student(id)

@app.put("/Students/{id}")
def update_Student(id: int, student: Students):
    return update_student(id, student)

@app.delete("/Students/{id}")
def delete_Student(id: int):
    return delete_student(id)

