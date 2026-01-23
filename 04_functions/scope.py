# nonlocal scope
chai_type = "ginger"


def upadte_order():
    chai_type = "elaichi"

    def kitchen():
        nonlocal chai_type
        # global chai_type
        chai_type = "black tea"
        print(chai_type)

    kitchen()
    print("after kitchen upadte", chai_type)


upadte_order()
