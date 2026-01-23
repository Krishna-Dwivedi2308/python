def chai_customer():
    print("Welcome to chai shop, what chai you would like ?")
    order=yield 
    while True:
        print(f"Preparing {order}")
        # order=yield

stall=chai_customer()
next(stall) #start the generator
stall.send("black tea")
stall.send("ginger")

