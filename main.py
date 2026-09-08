from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


@app.get("/")
def read_root():
    return{"message":"Hello World"}

@app.get("/about")
def read_about():
    return{"message":"This is the about page"}
@app.get("/greet/{name}")
def greet_name(name:str,age:int):
    return{"message":f"my name is {name},iam {age} years old"}

class Student(BaseModel):
    name:str
    age:int
    roll:int
@app.post("/create_student")
def create_student(student:Student):
    return{
        "name":student.name,
        "age":student.age,
        "roll":student.roll
    }
