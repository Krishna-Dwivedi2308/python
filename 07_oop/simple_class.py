class Chai:
    pass
class Chai_type:
    pass
print(type(Chai))
# <class 'type'>
# although this says class but always remember that everything in python is an object. so interrnally it is an object .
giner_tea=Chai()
print(type(giner_tea)) #<class '__main__.Chai'>
print(type(giner_tea) is Chai) #True
print(type(giner_tea) is Chai_type) #False
