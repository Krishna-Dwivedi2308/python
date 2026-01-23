# tuples are immutable
# list is mutable
# tuples are faster than lists
# tuples are hashable

# A tuple containing three spice names
# Tuples are ordered and immutable collections
masala_tuple = ("cumin", "pepper", "salt")

# Printing the tuple and its type
print(masala_tuple)
print(type(masala_tuple))  # <class 'tuple'>

# -------------------------------------------------
# ❌ INCORRECT APPROACH (commented for reference)
# -------------------------------------------------
# The following does NOT work because:
# - Variables on the RIGHT side of '=' must already exist
# - a, b, c are not defined yet, so this would raise NameError
#
# keys = (a, b, c)
# keys = masala_tuple

# -------------------------------------------------
# ✅ CORRECT APPROACH: TUPLE UNPACKING
# -------------------------------------------------
# Tuple unpacking assigns each element of the tuple
# to a variable on the LEFT side, position-wise
a, b, c = masala_tuple

# Now the variables are created and hold values
print(a)  # cumin
print(b)  # pepper
print(c)  # salt

# now we can also check membership
print("salt" in masala_tuple)  # True
print("Salt" in masala_tuple)  # False
