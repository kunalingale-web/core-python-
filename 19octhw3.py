class Car:
    def __init__(self, b, c, s, f):
        self.brand = b
        self.color = c
        self.speed = s
        self.fuel = f



car1 = Car("Toyota", "Black", 120, "Petrol")
car2 = Car("BMW", "White", 180, "Diesel")

print(car1.brand)
print(car1.color)
print(car1.speed)
print(car1.fuel)

print(car2.brand)
print(car2.color)
print(car2.speed)
print(car2.fuel)
