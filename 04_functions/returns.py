# def make_chai():
#     return 1,2,3
# # a,b=make_chai()

#     a,b=make_chai()
#     ^^^
# ValueError: too many values to unpack (expected 2)


def make():
    return 1, 2, 3, 4


a, b, _, _ = (
    make()
)  # _ is a dummy variable which is used if you don't want to use the other values right now so you don't assign a variable to it
print(a, b)
