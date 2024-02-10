class Fruit:
    __slots__ = ['name', 'caloies']
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

def __eq__(self, other):
    return self.__dict__ == other.__dict__

def __repr__ (self):
    return f"this is a {self.name} with {self.calories}"


banana = Fruit('Banana', 10)
apple = Fruit('Apple', 20)

print(banana.name)
print(apple.name)
print(banana.calories)
print(apple.calories)


class Fruitd:
    name: str
    calories: float


bananad = Fruitd()
appled = Fruitd()

print(bananad)
