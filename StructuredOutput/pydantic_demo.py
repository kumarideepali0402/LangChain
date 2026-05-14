from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str ='Deepali'       #default value
    age: Optional[str ]='18'
    email: EmailStr
    cgpa: float= Field(gt=0, lt=10, default =5, description="decimal value represeting cgpa of student")

new_student = {'name': "Nitish", "email": "deepali@f.com", "cgpa": 10}

student = Student(**new_student)

print(type(student));
print(student)

student_json = student.model_dump_json()

#type coercion is done by pydantic