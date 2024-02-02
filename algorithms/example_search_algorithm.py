from dataclasses import dataclass

@dataclass(kw_only=True)
class Person:
    firstname: str
    lastname: str
    id: int
    age: int

# Create a list of Person objects
people = [
    Person(firstname="John", lastname="Doe", id=1, age=30),
    Person(firstname="Jane", lastname="Doe", id=2, age=25),
    Person(firstname="Jim", lastname="Smith", id=3, age=35),
    Person(firstname="Jill", lastname="Johnson", id=4, age=40),
]

# Linear search function
def find_person_by_id(people, id):
    for person in people:
        if person.id == id:
            return person
    return None

# Test the search function
person = find_person_by_id(people, 3)
if person:
    print(person)
else:
    print("Person not found.")