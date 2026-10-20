class WashingMachine:
    def __init__(self, b, c, co, p):
        self.brand = b
        self.capacity = c
        self.color = co
        self.price = p

    


machine1 = WashingMachine("Samsung", "7kg", "White", 15000)
machine2 = WashingMachine("LG", "8kg", "Black", 20000)

print(machine1.brand)
print(machine1.capacity)
print(machine1.color)
print(machine1.price)

print(machine2.brand)
print(machine2.capacity)
print(machine2.color)
print(machine2.price)

