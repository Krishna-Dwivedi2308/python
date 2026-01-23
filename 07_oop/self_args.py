class Chaicup:
    size=150
    def describe(self):
        print(self.size) #150
        print(self) #<__main__.Chaicup object at 0x000001FB2F2A4A20>
        return f"A {self.size} ml chai cup"

cup=Chaicup()
print(cup.describe()) #A 150 ml chai cup
# print(Chaicup.describe()) => TypeError: describe() missing 1 required positional argument: 'self'
print(Chaicup.describe(cup)) #this will work correctly 