sugar_amount = 5

print("id of 1st value",id(sugar_amount))
print(sugar_amount)

sugar_amount =12
print("id of 2nd value",id(sugar_amount))
print(sugar_amount)

# now the question is whether it chnaged or not ?
# ANS: NO

# OUTPUT
# id of 1st value 140704904907320
# 5
# id of 2nd value 140704904907544
# 12
# we can see that the reference is changed not the actual value, it just points to a different address now , the initial value "5" is still there somewhere in memory .
# Hence, 'immutable'

spice_mix=set()
print(spice_mix)
print(id(spice_mix))

spice_mix.add("cumin")
print(spice_mix)
spice_mix.add("pepper")
print(spice_mix)
spice_mix.add("salt")

print(spice_mix)
print(id(spice_mix))

# OUTPUT:
# set()
# 1553633911392
# {'cumin'}
# {'cumin', 'pepper'}
# {'cumin', 'pepper', 'salt'}
# 1553633911392
# in this case , the id of the set has not changed, so this is pointing to the same memory address all throughout , but we are constanrtly adding new values , so the set is changing. Hence, 'mutable'