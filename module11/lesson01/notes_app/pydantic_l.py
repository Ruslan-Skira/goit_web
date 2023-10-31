from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name: str
    email: EmailStr
    surname: str
    age: Optional[int] = Field(None, ge=16, le=95)
    friends: Optional[int] = 0


victor = Student(
    name="Victor", email="victor.good_job@test.com", surname="Surname", age=20
)

print(victor)
sasha = Student(
    name="Sasha", email="sasha.good_job@test.com", surname="Surname", age=24
)
print(sasha)
