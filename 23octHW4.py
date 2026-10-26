# multiple inheritance 


class parent_a():
    def P_A_M(self):
        print("PARENT A method run ")
                                                # PARENT1 <-----CHILD-------> PARENT2

class parent_b():
    def P_B_M(self):
        print("PARENT B method run ") 

class child(parent_a,parent_b):
    def C_M(self):
        print("CHILD method run ")


obj1 = parent_a()
obj1.P_A_M()


# ERROR
# obj1.P_B_M() , obj1.C_M()
# 'parent_a' object has no attribute 'P_B_M'/C_M


obj2 = parent_b()
obj2.P_B_M()


# ERROR
# obj1.P_A_M() , obj1.C_M()
# 'parent_b' object has no attribute 'P_A_M'/C_M

obj3 = child()
obj3.C_M()
obj3.P_A_M()
obj3.P_B_M()
