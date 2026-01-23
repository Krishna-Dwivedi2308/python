from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return wrapper


@log_activity
def say_whee():
    print("Whee!")


say_whee()
