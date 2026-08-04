from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

user = User(name='Alice', age=30, email='alice@abc.corp')
print(user)
print(user.name)
print(user.age)
print(user.email)
