from dataclasses import dataclass

class Fruit:
    def __init__(self, name, calories) -> None:
        # print(f'Creating Fruit: name={name}, calories={calories}')
        self.name = name
        self.calories = calories

    def __eq__(self, other) -> bool:
        # print(f'Comparing for equality {self} with {other}')
        if isinstance(other, Fruit):
            return self.name == other.name and self.calories == other.calories
        return False

    def __repr__(self) -> str:
        return f'Fruit(name={self.name}, calories={self.calories})'

    def __str__(self):
        return f'{self.name}: {self.calories} calories'

    def __hash__(self) -> int:
        return hash((self.name, self.calories))

@dataclass
class Fruit:
    name: str
    calories: int

def main():
    banana = Fruit(name='Banana', calories=105)
    apple = Fruit(name='Apple', calories=95)

    print('banana:', banana)
    print('banana repr', repr(banana))
    print('banana str', str(banana))
    print('apple:', apple)
    print('apple repr', repr(apple))
    print('apple str', str(apple))

if __name__ == '__main__':
    main()