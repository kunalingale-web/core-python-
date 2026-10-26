# single inheritance(ONE SUPER CLASS & ONE SUB CLASS )


class parent : 
    def method_m1(self):
        print("super class method_m1..........")                           
        
        
                                                                ##   parent <----- child



class child (parent):
    def method_m2(self):
        print("sub class method_m2......")




obj = parent()
obj.method_m1()
    #error
# obj.method_m2() 
# ['parent' object has no attribute 'method_m2']   


obj = child()
obj.method_m2()
obj.method_m1() 


# #




                    
                 











