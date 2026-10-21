class HP_Gas_Cylinder:
    def __init__(self, b, w, g, p):
        self.brand = b
        self.weight = w
        self.gas_type = g
        self.price = p

    


cylinder1 = HP_Gas_Cylinder("HP Gas", "14.2 ", "LPG", 900)
cylinder2 = HP_Gas_Cylinder("Cjp Gas", "9 kg", "LPG", 200)
cylinder3 = HP_Gas_Cylinder("Bjp Gas", "12.5 kg", "LPG", 500)
cylinder4 = HP_Gas_Cylinder("Vvip Gas", "2 kg", "LPG", 1500)
cylinder5 = HP_Gas_Cylinder("Yjp Gas", "20 kg", "LPG", 2500)

cylinder_list = []


cylinder_list.append(cylinder1)
cylinder_list.append(cylinder2)
cylinder_list.append(cylinder3)
cylinder_list.append(cylinder4)
cylinder_list.append(cylinder5)


for cylinder in cylinder_list:
    if cylinder.weight >= "20":
        print(f"it is heavy cylinder {cylinder.brand,cylinder.weight,cylinder.price}")
    elif cylinder.weight >= "10":
        print("medium cylinder",cylinder.brand,)
    else:
        print("light cylinder")    








