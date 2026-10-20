class Flat:
    def __init__(self, n, l, b, p, a):
        self.name = n
        self.location = l
        self.bedroom = b
        self.price = p
        self.area = a



flat1 = Flat("Tower1", "Chandrapur", 2, 150000, "1000 sq.ft")
flat2 = Flat("Tower2", "nagpur", 4, 250000, "1700 sq.ft")

print(flat1.name)
print(flat1.location)
print(flat1.bedroom)
print(flat1.price)
print(flat1.area)

print(flat2.name)
print(flat2.location)
print(flat2.bedroom)
print(flat2.price)
print(flat2.area)

