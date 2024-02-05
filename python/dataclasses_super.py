from dataclasses import dataclass


@dataclass(frozen=True)
class Animal():
    color: str

    def make_sound(self):
        raise NotImplementedError("This method must be implemented by a subclass")

@dataclass(frozen=True)
class Pet(Animal):
    name: str

class Dog(Pet):
    breed: str
    def make_sound(self):
        return "Woof!"

class Cat(Pet): 
    def make_sound(self):
        return "Meow!" 

c = Cat(color="Black", name="Whiskers")

