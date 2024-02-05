
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal's name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        print(f"Dog's breed: {self.breed}")
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        print(f"Cat's color: {self.color}")

# Create instances to see the order of method calls
print("Creating Dog instance:")
d = Dog("Rex", "German Shepherd")

print("\nCreating Cat instance:")
c = Cat("Whiskers", "Black")

