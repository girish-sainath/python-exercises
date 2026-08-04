class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old."

def get_person_name(person: Person) -> str:
    return person.name

person1 = Person("Alice", 30)
print(person1.greet())
print(get_person_name(person1))