# ACCESSING BASE CLASS:
# 1. CODE DUPLICATION
# 2. EXPLICIT CALL
# 3. SUPER()


class Chai:
    def __init__(self, chai_type, strength):
        self.chai_type = chai_type
        self.strength = strength


class GingerChai(Chai):
    # code duplication
    def __init__(self, chai_type, strength, spiceLevel):
        self.chai_type = chai_type
        self.strength = strength
        self.spiceLevel = spiceLevel


class GingerChai(Chai):
    def __init__(self, chai_type, strength, spiceLevel):
        # explicit call
        Chai.__init__(self, chai_type, strength)
        self.spiceLevel = spiceLevel


class GingerChai(Chai):
    def __init__(self, chai_type, strength, spiceLevel):
        # super()
        super().__init__(chai_type, strength)
        self.spiceLevel = spiceLevel
