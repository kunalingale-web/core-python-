 #multi-level inheritance


class grandparent():
    def GP_m1(self):
        print("GP method run successfully.......")             
                                                                       #GRANDPARENT <-------PARENT <-------CHILD

class parent (grandparent):
    def P_m2(self):
        print("P method run successfully........")   

class child (parent):
    def C_m3(self):
        print("C method run successfully........") 


obj1 = grandparent()
obj1.GP_m1()

       # ERROR 
#obj1.P_m2() , obj1.C_m3()
#['grandparent' object has no attribute 'P_m2'/ 'C_m3']

obj2 = parent()
obj2.P_m2()
obj2.GP_m1()

        # ERROR
#obj2.C_m3() 
#'parent' object has no attribute 'C_m3'   


obj3 = child()
obj3.GP_m1()
obj3.P_m2()
obj3.C_m3()