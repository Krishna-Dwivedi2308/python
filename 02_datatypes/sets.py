essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# union
all_spices = essential_spices | optional_spices
print(
    f"All spices: {all_spices}"
)  # {'ginger', 'cardamom', 'cinnamon', 'cloves', 'black pepper'} : note that we did not add 'ginger' twice just like we do in sets in maths

# intersection
common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")  # {'ginger'} => common to both

# difference
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

# membership
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")
