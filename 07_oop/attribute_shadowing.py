class Chai:
    temperature="HOT"
    strength="Strong"

cutting=Chai()
print(cutting.temperature)
print(cutting.strength)
cutting.temperature="COLD"
cutting.cup='small'
print(cutting.temperature)
print(cutting.cup)
print(Chai.temperature)
# but what if we now delete the cutting.temperature attribute and then try to access it ?
del cutting.temperature
print(cutting.temperature) #HOT => it again falls back to the original value of the parent class 

# del cutting.cup => but if this cup attribute is deleted , it will not fall back to the parent class because it has nothing to fall back to

