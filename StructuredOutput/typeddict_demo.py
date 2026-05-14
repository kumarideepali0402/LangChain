from typing import TypedDict

class Person(TypedDict):
    name: str
    roll: int

user :Person = {'name': "deepali", 'roll': '1'}
# user :Person = {'name': "deepali", 'roll': 1} even this wont thro error

print(user)