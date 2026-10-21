class Car:
    def __init__(self, b, c, s, f):
        self.brand = b
        self.color = c
        self.speed = s
        self.fuel = f



car1 = Car("Toyota", "Black", 120, "Petrol")
car2 = Car("BMW", "White", 180, "Electric")
car3 = Car("SKODA", "Blue", 160, "Lpg")
car4 = Car("MARUTI", "Green", 110, "Cng")
car5 = Car("HUNDAI", "Orange", 130, "Petrol")

car_list = [car1,car2,car3,car4,car5]

for car in car_list :
    if car.speed <= 160 :
         print(car.brand,car.speed,car.color,car.fuel)
   

