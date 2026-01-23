# -------------------------------
# ENUMERATE FUNCTION
# -------------------------------

list1=['hello','world','python']
for index,element in enumerate(list1): #enumerate function returns a tuple of index and element like (0,'hello') and we can unpack it like this using two variables 
    print(index,element)

# OUTPUT
# 0 hello
# 1 world
# 2 python


# -------------------------------
# ZIP FUNCTION
# -------------------------------

list1=[1,2,3]
list2=['a','b','c']
for x,y in zip(list1,list2):
    print(x,y)

# OUTPUT
# 1 a
# 2 b
# 3 c

# -------------------------------
# FOR-ELSE LOOP
# -------------------------------

# this loop has a very specific use case . the else part runs only if the for loop does not break .
nums = [2, 4, 6, 8]

for n in nums:
    if n == 5:
        print("Found")
        break
else:
    print("Not found")
