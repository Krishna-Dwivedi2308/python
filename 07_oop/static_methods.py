# class ChaiUtils:
#     def cleanIngredients(self,text):
#         return [item.strip() for item in text.split(",")]

# raw="water,milk,ginger"
# obj=ChaiUtils()
# result=obj.cleanIngredients(raw)
# print(result)
            
class ChaiUtils:
    @staticmethod #now this is a statatic method , this does not need a self argument
    def cleanIngredients(text):
        return [item.strip() for item in text.split(",")]

raw="water,milk,ginger"
result=ChaiUtils.cleanIngredients(raw)
print(result)
            