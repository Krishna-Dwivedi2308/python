class BaseChai:
    def __init__(self,type_):
        self.type=type_
    def prepare(self):
        print(f"Preparing the {self.type} chai")

class MasalaChai(BaseChai):
        def add_spices(self):
            print("Adding spices")
            print("Adding masala powder")
class ChaiShop:
    chai_cls=BaseChai #this is not creating pbjects it is just storing the class in a variable

    def __init__(self):
        self.chai=self.chai_cls("regular")

    def serve(self):
        print(f"serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls=MasalaChai