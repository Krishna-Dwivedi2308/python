# Method Resolution Order
# Method Resolution Order (MRO) is the order in which Python looks for a method in a class hierarchy.
class A:
    label='A:Base Class'

class B(A):
    label='B:Derived Class from A'

class C(A):
    label='C:Derived Class from A'

class D(C,B): #here the order matters a lot 
    pass

cup=D() #C:Derived Class from A => this happens because we wrote C first in defining the class D(C,B)
print(cup.label)
print(cup.label)
# D:Derived Class from B and C
print(D.mro())
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]