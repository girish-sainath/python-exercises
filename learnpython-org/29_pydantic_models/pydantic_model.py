from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": 123,
    "name": "Zack Jonas",
    "signup_ts": "2024-06-01 12:23",
    "friends": [1, 2, 3]
}

user = User(**external_data)
print(user)
print(user.id)
print(user.name)
print(user.signup_ts)
print(user.friends)