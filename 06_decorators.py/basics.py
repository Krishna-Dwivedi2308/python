def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()
print(
    say_whee.__name__
)  # wrapper => now this should ideally not happen , i.e , the metadata about the function has changed by using decorator , to solve this problem , we will use a library called functools and import wraps from it .

from functools import wraps  # entire job of this is to preserve the metadata


def my_decorator(func):
    @wraps(func)  # this new line is added
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


say_whee()
print(say_whee.__name__)  # say_whee
