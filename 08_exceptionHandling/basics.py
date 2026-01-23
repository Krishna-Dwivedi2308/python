orders=['masala chai','ginger chai','cinnamon chai']
# print(orders[3]) #IndexError: list index out of range

# now we have a lot of such errors 
# some of them are :
# key error , name error , zero division error , type error 
#  no need to remember them , we figure out the error and handle it as per usage 

try:
    print(orders[3])
except IndexError: # this is called exception handling, this part will run and will print the message without crashing the code 
    print("Index Error")
except KeyError:
    print("Key Error")
except NameError:
    print("Name Error")
except ZeroDivisionError:
    print("Zero Division Error")
except TypeError:
    print("Type Error")