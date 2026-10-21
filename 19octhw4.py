class WashingMachine:
    def __init__(self, b, c, co, p):
        self.brand = b
        self.capacity = c
        self.color = co
        self.price = p

    


machine1 = WashingMachine("Samsung", "7kg", "White", 15000)
machine2 = WashingMachine("IFB", "8kg", "A-Black", 22000)
machine3 = WashingMachine("DDE", "9kg", "B-Black", 30000)
machine4 = WashingMachine("AAB", "14kg", "C-Black", 44000)
machine5 = WashingMachine("OOP", "12kg", "D-Black", 51000)


machine_list = []
machine_list.append(machine1)
machine_list.append(machine2)
machine_list.append(machine3)
machine_list.append(machine4)
machine_list.append(machine5)


for machine in machine_list:
    if machine.price >= 30000:
        print(f"we have lots of opetion in 30000 or more than 30000 price range {machine.brand,machine.capacity}")



