from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {"name": "Deepak", "age": "3"}

print(type(new_person))
print(new_person)
