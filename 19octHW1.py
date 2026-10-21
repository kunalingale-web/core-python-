class  Oats:
    def __init__(self,b,f,w,p1,p2):
        self.brand = b
        self.flavour = f
        self.weight = w
        self.price = p1
        self.protin= p2

pro1 = Oats("Alpino","Dark Chocolate","1kg",450,"27 G")
pro2 = Oats("Alpino"," Kesar","2kg",750,"29 G") 
pro3 = Oats("Alpino","Pista","3kg",910,"29 G")       
pro4 = Oats("Alpino","apple","4kg",1400,"29 G")
pro5 = Oats("Alpino","nuts","5kg",1600,"29 G")


oats_list =[pro1,pro2,pro3,pro4,pro5,pro1,pro2]


for oats in oats_list:
    if oats.price >= 750:
        print(oats.flavour,oats.weight)





