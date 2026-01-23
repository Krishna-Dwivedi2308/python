def local_chai():
    yield "black tea"
    yield "ginger chai"


def imported_chai():
    yield "matcha"
    yield "Oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
            print(f"Preparing {order}")
    except:
        print("Chai stall closed")


stall = chai_stall()
print(next(stall))
stall.close()  # this is also a cleanup , so always do this manually
