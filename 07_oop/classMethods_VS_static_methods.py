class ChaiOrder:
    def __init__(self, tea, milk, sugar):
        self.tea = tea
        self.milk = milk
        self.sugar = sugar

    @classmethod
    def from_dict(cls, order_data):        
        return cls(
            order_data['tea'],
            order_data['milk'],
            order_data['sugar']                   
                   )
    @classmethod
    def from_string(cls,order_string):
        tea,milk,sugar=order_string.split(",")
        return cls(tea,milk,sugar)

order1=ChaiOrder.from_dict({"tea":"Darjeeling","milk":"Yes","sugar":"Low"})
print(order1.__dict__)

order2=ChaiOrder.from_string("Green,Yes,Medium")
print(order2.__dict__)

# OUTPUT
# {'tea': 'Darjeeling', 'milk': 'Yes', 'sugar': 'Low'}
# {'tea': 'Green', 'milk': 'Yes', 'sugar': 'Medium'}

class chaiUtils:
    @staticmethod
    def cleanIngredients(text):
        return [item.strip() for item in text.split(",")]