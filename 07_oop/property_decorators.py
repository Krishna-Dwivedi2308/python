class teaLeaf:
    def __init__(self,age):
        self._age=age #this underscore is a way of saying this is a special variable and we are going to do something different with it 

    @property
    def age(self):
        return self._age+2
    
    @age.setter
    def age(self,age):
        if 1<=age<=5:
            self._age=age
        else:
            raise ValueError("Age must be between 1 and 5")

    @age.deleter
    def age(self):
        del self._age
leaf=teaLeaf(3)
print(leaf.age)
leaf.age=4
print(leaf.age)
leaf.age=6
print(leaf.age)

