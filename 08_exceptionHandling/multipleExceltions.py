def process_order(item, qty):
    try:
        price = {"masala": 20}[item]
        cost = int(price) * int(qty)
        print(f"total cost is {cost}")
        print(f"Processing order for {qty} {item} ")
    except KeyError:
        print("sorry that chai is not on the menu")
    except TypeError:
        print("qty must be a number")
    except:
        print("something went wrong")


process_order("masala", 2)
process_order("ginger", 2)
process_order("masala", "two")
