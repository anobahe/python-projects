def add(*args):
    num = 0
    for i in args:
        num += i
    return num


print(add(5, 3, 9, 10, 78, 100))


def calculate(**kwargs):
    print(kwargs["add"])


calculate(add=5, subt=10, mult=2)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("model")
        self.model = kwargs.get("make")



my_car = Car(model="GT-L", make="Toyota")
print(my_car.model)
