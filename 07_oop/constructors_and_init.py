class Chai_order:
    def __init__(self, tea, milk, sugar):  # constructor => name must always be __init__
        self.tea = tea
        self.milk = milk
        self.sugar = sugar

    def summary(self):
        return f"Tea: {self.tea}, Milk: {self.milk}, Sugar: {self.sugar}"


order1 = Chai_order("Darjeeling", "Yes", "Low")
print(order1.summary())

order2 = Chai_order("Green", "No", "Medium")
print(order2.summary())
