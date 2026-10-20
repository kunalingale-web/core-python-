class HP_Gas_Cylinder:
    def __init__(self, b, w, g, p):
        self.brand = b
        self.weight = w
        self.gas_type = g
        self.price = p

    


cylinder1 = HP_Gas_Cylinder("HP Gas", "14.2 kg", "LPG", 900)
cylinder2 = HP_Gas_Cylinder("HP Gas", "5 kg", "LPG", 500)

print(cylinder1.brand)
print(cylinder1.weight)
print(cylinder1.gas_type)
print(cylinder1.price)

print(cylinder2.brand)
print(cylinder2.weight)
print(cylinder2.gas_type)
print(cylinder2.price)

