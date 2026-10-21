class Flat:
    def __init__(self, n, l, b, r, a):
        self.name = n
        self.location = l
        self.bedroom = b
        self.rent = r
        self.area = a



flat1 = Flat("Tower1", "Chandrapur", 1, 15000, "1200 sq.ft")
flat2 = Flat("Tower2", "nagpur", 2, 25000, "1500 sq.ft")
flat3 = Flat("Tower3", "delhi", 3, 35000, "1400 sq.ft")
flat4 = Flat("Tower4", "mumbai", 4, 45000, "1600 sq.ft")
flat5 = Flat("Tower5", "pune", 5, 55000, "1900 sq.ft")

flat_list = [flat1,flat2,flat3,flat4,flat5]


for flat in flat_list:
    if flat.location == "pune":
        #print(flat.location,flat.rent,flat.area,flat.bedroom)
        print(f"the flat located in  {flat.location} and the rent is {flat.rent} and  bedroom availabe in flat is {flat.bedroom}")


