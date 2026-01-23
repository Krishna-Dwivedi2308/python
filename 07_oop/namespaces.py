class Chai:
    origin = "India"  # property of this class


print(Chai.origin)
Chai.is_hot = True
print(Chai.is_hot)
masala = Chai()
print("from msaala object")
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(masala.is_hot)
print(Chai.is_hot)  # the value changed in the object but not in the class

masala.flavoured = True
print(masala.flavoured)  # True
print(Chai.flavoured)  # but did not get added in the original class
