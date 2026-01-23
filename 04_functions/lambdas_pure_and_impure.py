# types of functions - pure and impure
# Pure functions - they do not have any side effects
def hello():
    a = 10
    print(a)


hello()
# Impure functions - they have side effects
a = 100


def impure():
    global a
    a = 11
    print(a)


impure()


# recursive functions
def pour_chai(n):
    if n == 0:
        print("Pouring chai")
        return
    pour_chai(n - 1)
    print("Poured chai")


pour_chai(10)
# lambdas - they do not have a name
chai_types = ["chai", "tea", "coffee", "tea"]

strong_chai = list(
    filter(lambda chai: chai != "tea", chai_types)
)  # filter takes first argument as a function and second argument as a list. now the function can be of any type . here we are filtering chai types which are not tea using a lambda function which is a temporary function which we would not want to use again
print(strong_chai)
