from typing import Annotated

def say_hello(name: Annotated[str, "The name of the person to greet"]) -> str:
    return f"Hello, {name}"

print(say_hello("Alice"))