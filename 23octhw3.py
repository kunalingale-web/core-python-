# Hierachical inheritance

class parent():
    def P_M(self):
        print("PARENT method run........")
                                                                # CHILD 1----->  PARENT  <------CHILD 2



class child_a(parent):
    def C_A_M(self):
            print("CHILD A method run........")



class child_b(parent):
     def C_B_M(self):
                 print("CHILD B method run........")



class child_c(parent):
      def C_C_M(self):
                       print("CHILD C method run........")

obj1 = parent()
obj1.P_M()

     # ERROR 
#obj1.C_A_M() , obj.C_B_M() , obj1.C_C_M()  
#'parent' object has no attribute 'C_A_M'/'C_B_M'/'C_C_M'    

obj2 = child_a()
obj2.P_M()
obj2.C_A_M()

     # ERROR
#obj2.C_B_M() , obj2.C_C_M() 
# 'child_a' object has no attribute 'C_B_M'/'C_C_M' 



obj3 = child_b()
obj3.P_M()
obj3.C_B_M()

     # ERROR
#obj2.C_A_M() , obj2.C_C_M() 
# 'child_b' object has no attribute 'C_A_M'/'C_C_M'    


obj4 = child_c()
obj4.P_M()
obj4.C_C_M()

     # ERROR
#obj2.C_A_M() , obj2.C_B_M() 
# 'child_c' object has no attribute 'C_A_M'/'C_B_M'   