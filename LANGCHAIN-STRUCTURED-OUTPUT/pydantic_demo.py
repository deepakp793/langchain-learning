from pydantic import BaseModel

class Student(BaseModel):
    name : str

new_student = Student(name='Deepak')

print(new_student)