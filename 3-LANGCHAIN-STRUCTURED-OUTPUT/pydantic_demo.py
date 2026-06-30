from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name: str
    age: int


new_student = Student(name="Deepak", age=31)

print(new_student)


class Employee(BaseModel):
    emp_name: str = "Deepak"
    emp_id: int
    emp_age: Optional[int] = None
    emp_role: str
    email: EmailStr
    emp_rating: float = Field(
        gt=0,
        lt=10,
        description="A decimal value representing employees annual performane",
    )


new_employee = {
    "name": "Deepak",
    "emp_id": "453",
    "emp_role": "Gen AI Engineer",
    "email": "deepak@AIEngineer.com",
    "emp_rating": "9.5",
}

employee = Employee(**new_employee)

print(employee)

emp_dict = employee.model_dump()
print(emp_dict["emp_role"])

emp_json = employee.model_dump_json()
print(emp_json)
