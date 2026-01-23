class Out_of_Ingredients_errors(Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise Out_of_Ingredients_errors("Out of Ingredients")
    else:
        print("Chai is ready")


make_chai(0, 1)
