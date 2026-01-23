chai_menu=["black tea","ginger","milk","water"]
try:
    chai=chai_menu[4]
    print(chai)
except:
    print("Chai not available")

print('this part would not print if error not handles gracefully ') #now imagine in production , rest of the program is not executed because the error crashed the program

def serveChai(flavour):
    try:
        print(f"preparing the {flavour} chai ")
        if flavour == "unknown":
            raise ValueError("Unknown Flavour") #it will print this message on console and trigger an error , stopping the further execution and will look for a matching except to handle the error 
    except ValueError as e:
        print(e)
    else:
        print("Chai served")
    finally:
        print("Chai stall closed")

serveChai("ginger")
serveChai("unknown")