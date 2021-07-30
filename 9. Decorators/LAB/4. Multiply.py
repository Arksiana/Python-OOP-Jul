def multiply(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for _ in range(times):
                return result * times
        return wrapper
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
