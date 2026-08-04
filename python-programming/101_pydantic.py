from pydantic import BaseModel, ValidationError

class User(BaseModel):
    name: str
    age: int
    email: str

try:
    user = User(name='Alice', age=30, email='alice@abc.corp')
except ValidationError as e:
    print('Validation error:', e)
else:
    print(user)
    print(user.name)
    print(user.age)
    print(user.email)